/* Shared read-only comparison view for Korean and Spanish pages. */
window.AuctionRecords = (() => {
  let data;
  const esc = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const cash = n => '$' + Number(n).toLocaleString('en-US');
  const words = {
    ko: {heading:'유사 차량 경매 기록',records:'건',all:'미국 전체',region:'기록 판매 주',city:'기록 판매 지역',allCities:'모든 지역',empty:'선택한 지역의 수집 기록이 없습니다.',shown:'표시 기록',sample:'집계 조건을 충족한 표본',range:'표본 가격 범위',median:'표본 중앙값',small:'표본 2건 미만: 중앙값 산출 안 함',ceiling:'기존 입찰 상한',gap:'상한 − 중앙값',vehicle:'차량·VIN·원문',sale:'판매일·지역',price:'기록 가격·판매 상태',options:'트림·사양·주행거리',damage:'타이틀·손상·작동',match:'대상과 차이 / 집계 처리',included:'집계 포함',excluded:'참고만 · 집계 제외',unknown:'미표시',different:'손상 다름',same:'신고 손상 일치',miles:'대상 대비 주행거리',rule:'집계: 동일 트림·타이틀, 주행거리 차이 40,000mi 이내, Run & drive, Sold + Reserve met Yes. 알려진 VIN·주행거리·구동·엔진·차체 문제 기록 제외. 손상 차이는 별도 표시하며 가격 보정은 하지 않았습니다.',limits:'FinalBid의 제3자 공개 기록이며 경매사 청구서로 독립 확인하지 않았습니다. 금액은 수수료·세금·운송·수리비 별도입니다. 희소한 편의표본으로 전체 시장 시세를 대표하지 않으며, 사진·엔진음 실사나 실시간 매물 상태 갱신 결과가 아닙니다.',checked:'기록 조회일',low:'유사 옵션도 손상·판매 지역·수리 범위가 다릅니다. 기존 상한을 올리는 근거로 쓰지 마세요.',error:'경매 기록을 불러오지 못했습니다. 새로고침하거나 비교 자료 JSON을 확인하세요.'},
    es: {heading:'Historial de subastas comparables',records:'registros',all:'Todo EE. UU.',region:'Estado de la venta',city:'Localidad de la venta',allCities:'Todas las localidades',empty:'No hay registros recopilados para esta región.',shown:'Registros mostrados',sample:'Muestra que cumple los criterios',range:'Rango de la muestra',median:'Mediana de la muestra',small:'Menos de 2 casos: no se calcula la mediana',ceiling:'Límite de oferta actual',gap:'Límite − mediana',vehicle:'Vehículo · VIN · fuente',sale:'Fecha · ubicación',price:'Precio registrado · estado',options:'Versión · motor · millas',damage:'Título · daño · condición',match:'Diferencias / tratamiento',included:'Incluido',excluded:'Sólo referencia · excluido',unknown:'No indicado',different:'Daño diferente',same:'Daño declarado coincidente',miles:'Diferencia de millas',rule:'Cálculo: misma versión y título, diferencia máxima de 40,000 mi, Run & drive, Sold y Reserve met Yes. Se excluyen problemas conocidos de VIN, odómetro, tracción, motor o carrocería. Los daños pueden diferir; no se ajustan los precios.',limits:'Registros públicos de FinalBid, sin verificación independiente mediante factura de la subasta. No incluyen tarifas, impuestos, transporte ni reparaciones. Es una muestra limitada, no una tasación del mercado. No implica inspección de fotos o sonido del motor ni actualización de disponibilidad.',checked:'Consultado',low:'Incluso con opciones similares, cambian los daños, la región y la reparación. Estos datos no justifican aumentar el límite de oferta.',error:'No se pudieron cargar los registros. Recargue la página o consulte el archivo JSON.'}
  };
  const flags = {
    buyNow:['Buy Now 별도 거래','Compra Buy Now'],statusConflict:['Sold / Reserve met No 불일치','Sold / Reserve met No contradictorios'],odometer:['주행거리 Not actual','Odómetro: Not actual'],titleUnknown:['타이틀 미표시','Título no indicado'],titleDifferent:['타이틀 다름','Título diferente'],trimDifferent:['트림 다름 또는 미확인','Versión diferente o no confirmada'],mileageGap:['주행거리 차이 40,000mi 초과','Diferencia superior a 40,000 mi'],runningUnknown:['Run & drive 미확인','Run & drive no confirmado'],driveDifferent:['구동방식 다름 또는 대상 미확인','Tracción diferente o no confirmada'],engineDifferent:['엔진 사양 다름','Motor diferente'],bodyUnverified:['차체 형식 일치 미확인','Carrocería coincidente no verificada']
  };
  function table(rows, summary, lang) {
    const w=words[lang], p=rows.filter(r=>r.included).map(r=>r.price).sort((a,b)=>a-b);
    const med=p.length>=2?(p[Math.floor((p.length-1)/2)]+p[Math.floor(p.length/2)])/2:null;
    let stats=`${w.shown}: ${rows.length} · ${w.sample}: ${p.length}`;
    if(p.length)stats+=` · ${w.range}: ${cash(p[0])}–${cash(p.at(-1))}`;
    stats+=`<br>${med===null?w.small:w.median+': '+cash(med)} · ${w.ceiling}: ${cash(summary.bidCeiling)}`;
    if(med!==null)stats+=` · ${w.gap}: ${summary.bidCeiling-med>=0?'+':'−'}${cash(Math.abs(summary.bidCeiling-med))}`;
    const body=rows.map(c=>`<tr><td><a href="${esc(c.source)}" target="_blank" rel="noopener">${esc(c.vehicle)} · #${esc(c.lot)}</a><br><small>${esc(c.vin)}</small></td><td>${esc(c.date)}<br>${esc(c.location)}<br><small>${w.checked}: ${esc(c.checkedAt)}</small></td><td><b>${cash(c.price)}</b><br>${esc(c.status)}<br>Reserve met: ${esc(c.reserveMet)}</td><td>${esc(c.trim||w.unknown)}<br>${esc(c.engine||w.unknown)} · ${esc(c.drive||w.unknown)}<br>${Number(c.miles).toLocaleString('en-US')} mi<br><small>${w.miles}: ${c.mileageDifference>=0?'+':''}${Number(c.mileageDifference).toLocaleString('en-US')} mi</small></td><td>${esc(c.title==='미표시'?w.unknown:c.title)}<br>${esc(c.damage)}<br>${esc(c.condition==='미표시'?w.unknown:c.condition)}</td><td>${c.included?w.included:w.excluded}<br>${c.damageMatch?w.same:w.different}${c.flags.length?'<br>'+c.flags.map(f=>esc(flags[f]?.[lang==='es'?1:0]||f)).join('<br>'):''}</td></tr>`).join('');
    return `<p class="record-stats" aria-live="polite">${stats}</p>${rows.length?`<div class="comps-scroll"><table><thead><tr>${[w.vehicle,w.sale,w.price,w.options,w.damage,w.match].map(x=>'<th scope="col">'+x+'</th>').join('')}</tr></thead><tbody>${body}</tbody></table></div>`:`<p role="status">${w.empty}</p>`}`;
  }
  function mount(root=document) {
    if(!data)return;
    root.querySelectorAll('.auction-slot:not([data-mounted])').forEach(slot=>{
      const lang=slot.dataset.lang==='es'?'es':'ko',w=words[lang];
      const s=data.summaries.find(x=>x.targetLot===slot.dataset.target);
      if(!s)return;slot.dataset.mounted='true';
      const rows=data.comparables.filter(x=>x.targetLot===s.targetLot);
      const states=[...new Set(['KS','MO',...rows.map(r=>r.state)])].sort();
      slot.classList.add('auction-comps');
      slot.innerHTML=`<details class="record-details"><summary>${w.heading} · ${rows.length} ${w.records}<span class="record-chevron" aria-hidden="true">⌄</span></summary><div class="record-content"><p>${w.low}</p><div class="record-filters"><label>${w.region}<select class="record-state"><option value="all">${w.all}</option>${states.map(x=>`<option value="${esc(x)}">${esc(x)}</option>`).join('')}</select></label><label>${w.city}<select class="record-city"></select></label></div><div class="record-table"></div><p class="comps-fine">${w.rule}</p><p class="comps-fine">${w.limits}</p></div></details>`;
      const state=slot.querySelector('.record-state'),city=slot.querySelector('.record-city'),out=slot.querySelector('.record-table');
      function refreshCities(){city.innerHTML=`<option value="all">${w.allCities}</option>`+[...new Set(rows.filter(r=>state.value==='all'||r.state===state.value).map(r=>r.location))].sort().map(x=>`<option value="${esc(x)}">${esc(x)}</option>`).join('');refresh();}
      function refresh(){out.innerHTML=table(rows.filter(r=>(state.value==='all'||r.state===state.value)&&(city.value==='all'||r.location===city.value)),s,lang);}
      state.addEventListener('change',refreshCities);city.addEventListener('change',refresh);refreshCities();
    });
  }
  const ready=fetch('auction-comps.json').then(r=>{if(!r.ok)throw Error(r.status);return r.json()}).then(d=>{data=d;mount();return d}).catch(()=>{document.querySelectorAll('.auction-slot').forEach(x=>{x.textContent=words[x.dataset.lang==='es'?'es':'ko'].error});return null;});
  return {ready,mount};
})();
