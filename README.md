# Kansas–Missouri car auction comparison

Copart 차량 비교 사이트입니다. 한국어·스페인어 목록, VIN 조사 기록, 유사 경매 비교 자료를 포함합니다.

## 사이트

- 통합 목록: https://dlwhdgus0810.github.io/ks-mo-car-auctions/combined.html
- 스페인어: https://dlwhdgus0810.github.io/ks-mo-car-auctions/es.html
- FB 마켓플레이스 비교: https://dlwhdgus0810.github.io/ks-mo-car-auctions/marketplace.html
- 캔자스 세단 원본: `dist/index.html`
- 캔자스 SUV 원본: `dist/suv.html`

## 자동 배포

`main` 브랜치에 커밋을 푸시하면 GitHub Actions가 `dist/` 폴더를 GitHub Pages에 배포합니다. GitHub 웹 편집기로 `main`에 저장해도 배포됩니다. 실행 결과는 저장소의 **Actions → Deploy car auction site**에서 확인합니다. 수동 재배포는 **Run workflow**를 사용합니다.

```sh
git add dist/
git commit -m "Update auction listings"
git push origin main
```

로컬 파일 저장만으로는 배포되지 않습니다. Copart 매물 조회도 자동 실행되지 않습니다. 차량 정보를 확인·수정하고 푸시해야 웹사이트가 갱신됩니다.

## 데이터 수정

- `dist/combined80.json`: 전체 차량 데이터. 파일명과 달리 80대 이상을 포함합니다.
- `dist/combined.html`: 한국어 통합 카드. JSON 데이터 수정 시 해당 HTML 카드도 함께 갱신합니다.
- `dist/es.html`: JSON을 읽는 스페인어 화면.
- `dist/copart-current.json`: 차량별 조회 시점의 판매 상태.
- `dist/auction-comps.json`: 유사 차량 경매 표본.
- `dist/marketplace-2026-09-23.json`: 2026-09-23 Facebook Marketplace 스냅샷(Overland Park 40mi, $0–$7,999). `dist/marketplace.js`가 통합 목록 카드와 `dist/marketplace.html`에 표시합니다.
- `scripts/`: 특정 날짜의 갱신 기록을 반영한 일회성 스크립트. 현재 데이터에 과거 스크립트를 다시 실행하지 마세요.

## 로컬 미리보기

```sh
python3 -m http.server 8766 --bind 127.0.0.1 --directory dist
```

http://127.0.0.1:8766/combined.html 을 엽니다.

## 자료의 범위

입찰가와 판매 상태는 카드별 조회 시점의 기록입니다. 비용은 조건부 예산이며 확정 견적이 아닙니다. 차량별 구매 자격·실차 상태를 확인해야 합니다. 사진·차량 정보의 권리는 원 제공자에게 있습니다.

기존 ChatGPT Sites 주소는 별도 배포본입니다. 이 저장소의 푸시는 GitHub Pages 주소에만 반영됩니다.
