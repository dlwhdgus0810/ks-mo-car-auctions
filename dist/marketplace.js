/* Facebook Marketplace snapshot next to the Copart lots: card blocks on combined.html, tables on marketplace.html. */
window.MarketCompare = (() => {
  let d;
  const esc = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const cash = n => '$' + Number(n).toLocaleString('en-US');
  const miles = n => Number(n).toLocaleString('en-US') + ' mi';
  const kmi = n => Math.round(n / 1000) + 'K';
  const range = (values, f = x => x) => {
    if (!values.length) return '—';
    const lo = Math.min(...values), hi = Math.max(...values);
    return lo === hi ? f(lo) : f(lo) + '–' + f(hi);
  };
  const TITLE = {clean:'클린 (판매자 기재)', rebuilt:'Rebuilt', salvage:'Salvage', unknown:'미기재'};
  const ORDER = {clean:0, unknown:1, rebuilt:2, salvage:3};
  const byTitle = (a, b) => a.avoid - b.avoid || ORDER[a.title] - ORDER[b.title] || a.price - b.price;
  const usable = x => x.title === 'clean' && !x.avoid;
  const total = x => { const c = d.costRule; return Math.ceil((x.price * (1 + c.taxRate) + c.registration + c.inspection + c.maintenance) / 100) * 100; };
  const cheapest = list => list.filter(usable).sort((a, b) => a.price - b.price)[0];
  const gap = n => n < 0 ? `FB가 ${cash(-n)} 낮음` : n > 0 ? `FB가 ${cash(n)} 높음` : '같음';
  const link = x => `<a href="https://www.facebook.com/marketplace/item/${esc(x.id)}/" target="_blank" rel="noopener">${esc(x.vehicle)} ↗</a>`;
  const scope = () => `${esc(d.search.center)} 반경 ${d.search.radiusMiles}mi · 호가 ${cash(d.search.priceMin)}–${cash(d.search.priceMax)} · ${esc(d.checkedAt)} 조회`;
  const rule = () => { const c = d.costRule; return `조건부 총액 = 호가 + 세금 ${c.taxRate * 100}% 적립 + 등록·검사 ${cash(c.registration)} + 구매 전 점검 ${cash(c.inspection)} + 초기 정비 ${cash(c.maintenance)}, $100 단위 올림. 흥정·보험·추가 수리비는 반영하지 않았습니다.`; };

  function table(list) {
    const rows = list.map(x => `<tr><td>${link(x)}${x.pick ? ' <b class="market-tag">추천</b>' : ''}${x.avoid ? ' <b class="market-tag warn">주의</b>' : ''}</td><td><b>${cash(x.price)}</b></td><td>${cash(total(x))}</td><td>${miles(x.miles)}</td><td>${TITLE[x.title]}</td><td>${esc(x.city)}<br><small>${x.days ? x.days + '일 전' : '오늘'} 게시</small></td><td>${esc([x.note, x.dealer && '딜러·업자 판매'].filter(Boolean).join(' · '))}</td></tr>`).join('');
    return `<div class="market-scroll"><table><thead><tr>${['FB 매물', '호가', '조건부 총액', '주행거리', '타이틀', '위치·게시', '판매자 설명 요약'].map(h => `<th scope="col">${h}</th>`).join('')}</tr></thead><tbody>${rows}</tbody></table></div>`;
  }

  function mountCards() {
    for (const card of document.querySelectorAll('article.vehicle[id^="lot-"]')) {
      const model = d.lots[card.id.slice(4)];
      if (!model || card.querySelector('.market-slot')) continue;
      const list = d.listings.filter(x => x.model === model).sort(byTitle);
      const slot = document.createElement('section');
      slot.className = 'auction-comps market-slot';
      if (!list.length) {
        slot.innerHTML = `<p class="market-empty">FB 마켓플레이스 ${esc(model)} 매물 없음 · ${scope()}</p>`;
      } else {
        const best = cheapest(list), cost = +card.dataset.cost;
        const bestLine = best ? `클린 기재 최저 조건부 총액 ${cash(total(best))} (${esc(best.vehicle)} · ${miles(best.miles)}) · 이 차 대비 ${gap(total(best) - cost)}` : '클린 타이틀로 기재된 매물 없음';
        slot.innerHTML = `<details class="record-details"><summary>FB 마켓플레이스 ${esc(model)} · ${list.length}건 · 클린 기재 ${list.filter(usable).length}건<span class="record-chevron" aria-hidden="true">⌄</span></summary><div class="record-content"><p class="record-stats">이 차 Copart 조건부 총액 ${cash(cost)} · FB 호가 ${range(list.map(x => x.price), cash)} · FB 연식 ${range(list.map(x => x.year))}<br>${bestLine}</p>${table(list)}<p class="comps-fine">${scope()}. ${rule()} 타이틀·주행거리·설명은 판매자 기재이며 실차·서류는 확인하지 않았습니다. <a href="marketplace.html">차종별 비교 전체 보기</a></p></div></details>`;
      }
      card.append(slot);
    }
  }

  async function mountPage() {
    const models = document.querySelector('#market-models');
    if (!models) return;
    const cars = await fetch('combined80.json', {cache:'no-store'}).then(r => { if (!r.ok) throw Error(r.status); return r.json(); });
    const current = c => !['sold', 'ended'].includes(c.availability) && !c.needsBroker;
    const groups = {};
    for (const c of cars) if (d.lots[c.id]) (groups[d.lots[c.id]] ||= []).push(c);
    const rows = Object.entries(groups).map(([model, all]) => {
      const cur = all.filter(current), fb = d.listings.filter(x => x.model === model);
      return {model, all, cur, fb, best: cheapest(fb)};
    }).filter(r => r.cur.length || r.fb.length).sort((a, b) => b.cur.length - a.cur.length || b.fb.length - a.fb.length);
    models.innerHTML = `<div class="market-scroll"><table><thead><tr>${['차종', 'Copart 현재 후보', 'Copart 조건부 총액', 'FB 매물 (클린 기재)', 'FB 호가', 'FB 클린 최저 총액', 'Copart 최저 총액 대비'].map(h => `<th scope="col">${h}</th>`).join('')}</tr></thead><tbody>${rows.map(r => {
      const low = r.cur.length ? Math.min(...r.cur.map(c => c.roundedTotal)) : null;
      return `<tr><td><b>${esc(r.model)}</b></td><td>${r.cur.length}대 / 전체 ${r.all.length}대${r.cur.length ? `<br><small>${range(r.cur.map(c => +c.vehicle.slice(0, 4)))}년식 · ${range(r.cur.map(c => c.miles), kmi)} mi</small>` : ''}</td><td>${range(r.cur.map(c => c.roundedTotal), cash)}</td><td>${r.fb.length}건 (${r.fb.filter(usable).length})${r.fb.length ? `<br><small>${range(r.fb.map(x => x.year))}년식 · ${range(r.fb.map(x => x.miles), kmi)} mi</small>` : ''}</td><td>${range(r.fb.map(x => x.price), cash)}</td><td>${r.best ? `${cash(total(r.best))}<br><small>${link(r.best)}</small>` : '—'}</td><td>${r.best && low !== null ? gap(total(r.best) - low) : '—'}</td></tr>`;
    }).join('')}</tbody></table></div>`;

    document.querySelector('#market-picks').innerHTML = table(d.listings.filter(x => x.pick).sort((a, b) => a.price - b.price));
    document.querySelector('#market-avoid').innerHTML = table(d.listings.filter(x => x.avoid));

    const model = document.querySelector('#market-model'), title = document.querySelector('#market-title'), out = document.querySelector('#market-all');
    const counts = {};
    for (const x of d.listings) counts[x.model] = (counts[x.model] || 0) + 1;
    model.innerHTML = `<option value="all">전체 차종</option>` + Object.keys(counts).sort().map(m => `<option value="${esc(m)}">${esc(m)} (${counts[m]})</option>`).join('');
    const render = () => {
      const list = d.listings.filter(x => (model.value === 'all' || x.model === model.value) && (title.value === 'all' || x.title === title.value)).sort(byTitle);
      document.querySelector('#count').textContent = `${list.length}건 표시`;
      out.innerHTML = list.length ? table(list) : '<p role="status">조건에 맞는 매물이 없습니다.</p>';
    };
    model.addEventListener('change', render);
    title.addEventListener('change', render);
    render();
    mountRank(cars);
  }

  /* One 100-point scale for Copart Kansas City lots (price = similar-auction average) and FB listings (price = asking). */
  const AVAIL = {live:'경매 진행', scheduled:'경매 예정', future:'Future · 날짜 미정', upcoming:'Upcoming · 입찰 전', sold:'판매 완료', ended:'종료 · 결과 미확인'};
  const FB_DOC = {clean:20, unknown:12, rebuilt:10, salvage:6};
  const copartDoc = damage => damage.includes('+') ? 3 : /mechanical/i.test(damage) ? 2 : /front|rear|side|roof|under/i.test(damage) ? 5 : 8;
  const scale = (v, best, worst, pts) => Math.round(Math.max(0, Math.min(1, (v - worst) / (best - worst))) * pts * 10) / 10;

  function mountRank(cars) {
    const out = document.querySelector('#market-rank');
    if (!out) return;
    const copart = cars.filter(c => c.yard === 'KC').map(c => ({
      source:'Copart KC', id:c.id, vehicle:c.vehicle, url:c.url, year:+c.vehicle.slice(0, 4), miles:c.miles,
      price:c.comparisonAverage == null ? null : Math.round(c.comparisonAverage), count:c.comparisonAverageCount, total:c.roundedTotal,
      doc:copartDoc(c.damage), docText:`KS Salvage · ${c.damage}`, status:(AVAIL[c.availability] || c.availability) + (c.finalBid ? ` · 낙찰가 ${cash(c.finalBid.price)}` : ''), closed:['sold', 'ended'].includes(c.availability)}));
    const fb = d.listings.map(x => ({
      source:'FB', id:x.id, vehicle:x.vehicle, url:`https://www.facebook.com/marketplace/item/${x.id}/`, year:x.year, miles:x.miles, price:x.price,
      doc:x.avoid ? 0 : FB_DOC[x.title], docText:[TITLE[x.title], x.note].filter(Boolean).join(' · '), status:`${x.days ? x.days + '일 전' : '오늘'} 게시`, closed:false, avoid:x.avoid}));
    const ranked = [...copart, ...fb].filter(e => e.price != null);
    for (const e of ranked) {
      e.parts = [scale(e.price, 500, 10000, 35), scale(e.year, 2024, 2008, 20), scale(e.miles, 30000, 230000, 25), e.doc];
      e.score = Math.round(e.parts.reduce((a, b) => a + b, 0) * 10) / 10;
    }
    ranked.sort((a, b) => b.score - a.score || a.price - b.price).forEach((e, i) => { e.rank = i + 1; });
    const missing = copart.filter(e => e.price == null);
    const top = ranked.slice(0, 20);
    document.querySelector('#rank-summary').textContent = `Copart KC ${copart.length}대(유사 경매 평균 있음 ${copart.length - missing.length}대) + FB ${fb.length}건 · 상위 20위 중 Copart ${top.filter(e => e.source !== 'FB').length}대, FB ${top.filter(e => e.source === 'FB').length}건`;
    const source = document.querySelector('#rank-source'), open = document.querySelector('#rank-open');
    const row = e => `<tr><td><b>${e.rank}</b></td><td><a href="${esc(e.url)}" target="_blank" rel="noopener">${esc(e.vehicle)} ↗</a>${e.avoid ? ' <b class="market-tag warn">주의</b>' : ''}<br><small>${esc(e.source)}${e.source === 'FB' ? '' : ' #' + esc(e.id)} · ${esc(e.status)}</small></td><td><b>${cash(e.price)}</b><br><small>${e.source === 'FB' ? '호가' : `유사 경매 평균 ${e.count}건 · 수수료 제외<br>조건부 총액 ${cash(e.total)} (순위 미반영)`}</small></td><td>${miles(e.miles)}</td><td>${esc(e.docText)}</td><td><b>${e.score}</b><br><small>가격 ${e.parts[0]} · 연식 ${e.parts[1]} · 주행 ${e.parts[2]} · 서류 ${e.parts[3]}</small></td></tr>`;
    const render = () => {
      const list = ranked.filter(e => (source.value === 'all' || (source.value === 'fb') === (e.source === 'FB')) && !(open.value === 'open' && e.closed));
      document.querySelector('#rank-count').textContent = `${list.length}대 표시`;
      out.innerHTML = `<div class="market-scroll"><table><thead><tr>${['순위', '차량', '비교 가격', '주행거리', '서류·손상', '점수 /100'].map(h => `<th scope="col">${h}</th>`).join('')}</tr></thead><tbody>${list.map(row).join('')}</tbody></table></div>${missing.length ? `<p class="comps-fine">유사 경매 기록이 없어 순위에서 뺀 Copart KC: ${missing.map(e => esc(e.vehicle) + ' #' + esc(e.id)).join(', ')}</p>` : ''}`;
    };
    source.addEventListener('change', render);
    open.addEventListener('change', render);
    render();
  }

  const ready = fetch('marketplace-2026-09-23.json', {cache:'no-store'})
    .then(r => { if (!r.ok) throw Error(r.status); return r.json(); })
    .then(json => { d = json; mountCards(); return mountPage(); })
    .catch(() => { const el = document.querySelector('#market-models'); if (el) el.textContent = 'FB 마켓플레이스 자료를 불러오지 못했습니다. 새로고침하거나 JSON 파일을 확인하세요.'; });
  return {ready};
})();
