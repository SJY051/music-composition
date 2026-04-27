[English](./README.md) | [한국어](./README.ko.md)

# Music Composition Agent Skill

![Version](https://img.shields.io/badge/version-1.0-blue) ![Docs License](https://img.shields.io/badge/docs-CC%20BY%204.0-green) ![Code License](https://img.shields.io/badge/code-MIT-blue) ![Compatibility](https://img.shields.io/badge/compatibility-any%20SKILL.md%20harness-orange)

AI 작곡 어시스턴트를 위한 모듈식 지식 / 워크플로 스킬.

이 저장소는 에이전트가 모호한 창작 요청 — "후렴이 더 강하게 꽂혔으면 좋겠어", "K-pop 브릿지를 좀 더 어둡게", "재즈처럼 리하모니제이션하되 너무 빽빽하지 않게", "내 플레이리스트 기준으로 레퍼런스 트랙 찾아줘" — 를 구체적인 음악적 결정으로 번역하도록 돕는다: 화성, 멜로디 형태, 그루브, 형식, 편곡 무브, 진단 피드백, 리서치 워크플로 등.

**현재 릴리스:** `v1.0`
**릴리스 날짜:** `2026-04-27`

---

## 설치

가장 간단한 방법은 [`skills` CLI](https://www.npmjs.com/package/skills) 사용 (Node.js 필요):

```bash
npx skills add SJY051/music-composition
```

현재 프로젝트의 에이전트 디렉토리(예: `.claude/skills/`)에 설치된다. 사용자 전역 설치는 `-g`, 프롬프트 없이 진행하려면 `--all -y`를 추가.

수동 설치 시에는 저장소를 클론한 뒤 에이전트가 참조하게 하거나, `SKILL.md`와 필요한 하위 디렉토리를 에이전트 스킬 폴더(예: `~/.claude/skills/` 또는 프로젝트의 `.claude/skills/`)로 복사한다:

```bash
git clone https://github.com/SJY051/music-composition.git
```

이 스킬은 SKILL.md 표준을 읽는 모든 하니스에서 작동한다 — Claude Code, Claude Agent SDK, Claude.ai (skills 기능), 그 외 대부분의 현재 에이전트 플랫폼 포함.

---

## 이 스킬은 어디에 쓰는가

AI 에이전트가 다음과 같은 작업을 도와야 할 때 사용한다:

- 작곡 브레인스토밍
- 코드 진행과 화성 방향 잡기
- 멜로디, 모티프, 프레이즈, 탑라인 작업
- 곡 형식, 전환, 서사 구조
- 리듬, 그루브, 박자, 필
- 오케스트레이션, 편곡, 보이싱, 악기 이디엄
- 팝 / 재즈 / 클래식 / 게임 / 미디어 / 지역 / 전통 / 하이브리드 스타일 전반의 장르 의식 작업
- 작업 중인 곡에 대한 비평과 수정
- 작곡 우선 관점의 음악 이론 교육
- 최신 음악 트렌드 리서치와 레퍼런스 트랙 디깅
- 여러 턴에 걸친 사용자–에이전트 협업 워크플로

이 스킬은 DAW, 오디오 엔진, MIDI 생성기, 트랜스크립션 엔진, 법률 서비스, 또는 특정 전통에 특화된 인간 전문가를 대체하는 도구가 **아니다**. 어디까지나 AI 어시스턴트를 위한 **구조화된 레퍼런스 / 워크플로 레이어**다.

---

## 핵심 설계 철학

이 스킬은 몇 가지 실용적 원칙 위에 세워졌다.

1. **작곡은 규칙 따르기가 아니라 의사결정이다.**
   음악 이론은 명령 목록이 아니라 가능한 효과의 지도로 다룬다.

2. **연주 가능하고 실행 가능한 출력.**
   코드 차트, 도수 멜로디, 그루브 스케치, 보이싱 제안, 수정 블록처럼 구체적인 예시를 우선한다.

3. **사용자의 주도권 보존.**
   여러 옵션을 제시하고, 트레이드오프를 설명하고, 방향 선택은 사용자에게 맡긴다.

4. **필요한 레퍼런스만 로드.**
   에이전트는 기본적으로 `SKILL.md`에서 시작 → `references/00-navigation.md`에서 라우팅 → 가장 관련성 높은 1–3개 파일만 로드한다.

5. **최신 음악 트렌드는 리서치 작업으로 다룬다.**
   정적 장르 파일은 안정적인 작곡 컨벤션을 제공한다. 최근 아티스트, 차트, 플랫폼 동향, 씬별 레퍼런스는 능동적 웹 리서치로 확인한다.

6. **얕은 문화적 단축은 피한다.**
   전통과 지역에 특화된 음악을 단순 "플레이버"로 환원하지 않는다. 전통, 기능, 언어, 리듬 시스템, 악기 편성, 협업 필요성을 명확히 명명하도록 유도한다.

---

## 저장소 구조

```text
.
├── SKILL.md
├── MAINTENANCE.md
├── RELEASE-ROADMAP.md
├── KNOWN-LIMITATIONS.md
├── RELEASE-NOTES-v1.0.md
├── VALIDATION-v1.0.md
├── assets/
├── references/
│   ├── 00-navigation.md
│   ├── creative-workflows/
│   ├── form/
│   ├── fundamentals/
│   ├── genres/
│   ├── harmony/
│   ├── instrument-idiom/
│   ├── melody/
│   ├── orchestration/
│   ├── production-aware/
│   ├── research/
│   ├── rhythm-groove/
│   ├── songwriting/
│   ├── techniques/
│   └── validation/
└── scripts/
    └── music_theory_sanity_check.py
```

### 주요 파일

| 파일 | 용도 |
|---|---|
| `SKILL.md` | 에이전트의 최상위 운영 지침. 여기서부터 시작. |
| `references/00-navigation.md` | 적절한 레퍼런스 파일을 고르기 위한 라우팅 맵. |
| `assets/` | 즉시 사용 가능한 짧은 치트시트와 응답 템플릿. |
| `references/creative-workflows/` | 브레인스토밍, 수정, 답변 캘리브레이션, 사용자–에이전트 협업. |
| `references/research/` | 웹 트렌드 리서치, 레퍼런스 트랙 디깅, 스트리밍 서비스 인지 리서치, 스타일/저작권 가드레일. |
| `references/genres/` | 장르 / 지역별 스타터 가이드. |
| `references/instrument-idiom/` | 작곡 관점에서의 연주 가능성과 이디엄 가이드. |
| `references/validation/` | 릴리스 준비도, 스모크 테스트, 정합성 패스, 패키징 체크리스트. |
| `scripts/music_theory_sanity_check.py` | 링크, 알려진 이론 오류, 위험 용어, 스냅샷 노트, 필수 파일에 대한 회귀 검사기. |

---

## 권장 에이전트 워크플로

대부분의 사용자 요청에 대해:

```text
1. SKILL.md를 읽는다.
2. references/00-navigation.md를 사용해 가장 작은 유용한 문서 집합을 식별한다.
3. 관련 레퍼런스 파일만 로드한다(보통 1–3개).
4. 구체적인 음악적 출력을 생성한다.
5. 왜 그 선택이 통하는지 설명한다.
6. 적은 수의 다음 옵션을 제시한다.
```

예를 들어:

| 사용자 요청 | 라우팅 |
|---|---|
| "슬프지만 진부하지 않은 진행 줘." | `harmony/functional-harmony.md`, `harmony/modal-harmony.md`, `assets/progressions-catalog.md` |
| "후렴이 안 꽂혀." | `assets/diagnostic-checklists.md`, `songwriting/hooks-and-memorability.md`, `production-aware/energy-and-dynamics.md` |
| "이 부분 기타로 더 치기 쉽게 해 줘." | `instrument-idiom/guitar.md` + 관련 화성 / 편곡 파일 |
| "방향성 세 가지 브레인스토밍해 줘." | `creative-workflows/musical-brainstorming.md`, `assets/musical-brainstorming-cards.md` |
| "최근 J-pop 레퍼런스 찾아 줘." | `research/web-music-trend-research.md`, `research/reference-track-digging.md`, `assets/web-search-cheatsheet.md` |
| "내 플레이리스트를 레퍼런스로 써 줘." | `research/user-listening-context-and-streaming-services.md`, `assets/trend-and-reference-matrices.md` |

---

## 최신성 정책

일부 파일에는 스냅샷 노트가 포함되어 있다. 이런 파일은 시간이 지나면서 낡을 수 있는 정보를 담고 있다 — 특히:

- 현재 장르 트렌드
- 차트와 스트리밍 플랫폼 동향
- 아티스트 레퍼런스
- 지역 씬
- AI 보조 음악 도구
- 저작권 / 정책 동향

스냅샷 노트는 "이 파일이 영구적으로 최신"이라는 의미가 아니라, 해당 날짜 기준으로 마지막 검토가 이루어졌다는 의미다. 새로운 클레임에는 리서치 문서를 활용하고 출처를 검증한다.

유용한 리서치 파일:

```text
references/research/web-music-trend-research.md
references/research/reference-track-digging.md
references/research/user-listening-context-and-streaming-services.md
references/research/regional-trend-evolution-analysis.md
references/research/style-reference-and-copyright.md
assets/web-search-cheatsheet.md
```

---

## 스타일, 오리지널리티, 저작권 가드레일

이 스킬은 **오리지널 음악 아이디어 생성**을 돕기 위한 것이다. 기존 곡이나 아티스트의 보호받는 표현을 복제하는 데 써서는 안 된다.

사용자가 특정 아티스트 / 곡 스타일을 요청하면, 에이전트는 그 레퍼런스를 다음과 같은 작업 변수로 번역한다:

- 템포 범위
- 그루브 타입
- 화성 밀도
- 형식
- 보컬 음역과 프레이징 스타일
- 편곡 밀도
- 악기 편성
- 에너지 곡선
- 프로덕션 시대 단서

다음과 같은 보호받는 요소는 복제 / 모방하지 않는다:

- 멜로디
- 가사
- 특징적인 리프
- 샘플
- 시그니처 프로듀서 태그
- 매우 구체적인 보컬 정체성
- 특정 녹음의 식별 가능한 편곡 시퀀스

참고:

```text
references/research/style-reference-and-copyright.md
KNOWN-LIMITATIONS.md
```

---

## 문화적 / 지역적 특수성

이 스킬에는 전통, 지역, 하이브리드 스타일에 대한 가이드가 포함되어 있다. 이들은 **작곡 관점의 스타터 레퍼런스**이지, 문화적 전문성, 모국어 지식, 실천자 협업을 대체하지 않는다.

문화적으로 특수한 자료를 다룰 때는 다음과 같이 명시한다:

```text
구체적 전통 / 지역 / 언어 / 기능 / 리듬 / 악기 이디엄 / 연주 맥락
```

다음과 같은 모호한 라벨을 피한다:

```text
포괄적 월드 플레이버 / 민족적 색깔 / 아시아 플레이버 / 중동 플레이버
```

관련 파일:

```text
references/genres/korean-traditional.md
references/genres/folk-roots-and-traditions.md
references/genres/mena-pop.md
references/genres/south-asian-film-pop.md
references/genres/regional-scene-starters.md
references/research/regional-trend-evolution-analysis.md
```

---

## 검증

v1.0 패키지는 다음 문서에 기록된 릴리스 검증을 통과했다:

```text
VALIDATION-v1.0.md
references/validation/first-release-readiness.md
references/validation/phase-b-correctness-pass.md
references/validation/phase-c-smoke-test-results.md
```

정합성 검사 실행:

```bash
python scripts/music_theory_sanity_check.py
```

검사기는 다음과 같은 문제를 잡는다:

- 끊어진 내부 마크다운 레퍼런스
- 알려진 고위험 음악 이론 회귀
- 위험한 문화적 단축 용어
- 최신성에 민감한 파일에서 누락된 스냅샷 노트
- 필수 릴리스 / 검증 파일 존재 여부
- 선택된 음정, 모드, 코드 표기, 알터드 도미넌트 정합성

이 검사기는 회귀 방지 도구이지, 음악적 정확성에 대한 완전한 증명이 아니다.

---

## 유지보수

저장소를 변경하기 전에:

1. `MAINTENANCE.md`를 읽는다.
2. 파일을 추가하거나 옮길 때 `references/00-navigation.md`를 갱신한다.
3. 사용 빈도가 높은 에셋은 간결하고 정확하게 유지한다.
4. 최신성에 민감한 파일에는 스냅샷 노트를 사용한다.
5. `scripts/music_theory_sanity_check.py`를 실행한다.
6. 의미 있는 검증 작업은 해당 검증 문서에 기록한다.

권장 버전 정책:

| 변경 유형 | 권장 버전 |
|---|---|
| 오타, 링크, 작은 검증 스크립트 수정 | `v1.0.x` |
| P0/P1 정합성 핫픽스 | `v1.0.x` 핫픽스 |
| 새 장르, 워크플로, 리서치 문서 | `v1.1` |
| 더 큰 파서 / 평가 하니스 개선 | `v1.1` 또는 `v1.2` |
| 주요 구조 변경 또는 파일 재구성 | `v2.0` 후보 |

---

## 알려진 한계

전체 목록은 `KNOWN-LIMITATIONS.md` 참조.

요약하자면, 이 스킬은 다음을 직접 제공하지 않는다:

- 오디오 트랜스크립션
- DAW 제어
- MIDI 익스포트
- 오디오 믹싱 / 마스터링
- 법률 자문
- 웹 리서치 없는 보장된 최신 트렌드 지식
- 모든 지역 / 전통 음악 실천에 대한 완전한 전문성

---

## 라이선스

이 저장소는 분리된 라이선스를 사용한다:

- 스킬 문서, 레퍼런스, 에셋, 릴리스 노트, 검증 문서는 **Creative Commons Attribution 4.0 International (CC BY 4.0)** 라이선스로 제공된다.
- `scripts/`의 코드는 **MIT License**로 제공된다.

자세한 내용은 `LICENSE.md` 참조.
