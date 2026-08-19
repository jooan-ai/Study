<div style="line-height: 2.5; font-size: 1.2em;">

# NumPy 주요 메서드 및 함수 정리 (기능별)
* 고성능 계산기 - 벡터, 행렬 계산용

## 1. 배열 생성 및 초기화 (Array Creation & Initialization)

* **<u>`np.array(object)`**: 파이썬 리스트/튜플 등의 object을 NumPy 배열(`ndarray`)로 변환
* **`np.zeros(shape)`**: 모든 원소가 0인 배열 생성
* **`np.ones(shape)` / `np.ones_like(A, dtype)`**: 모든 원소가 1인 배열 생성 / 다른 배열 A의 크기 형태를 따라서 1로 채워진 배열 생성 
* **`np.full(shape, fill_value)`**: 지정한 특정 값으로 채워진 배열 생성
* **`np.arange([start,] stop[, step])`**: 지정한 범위와 간격의 연속된 숫자 배열 생성
* **`np.linspace(start, stop, num)`**: 지정한 범위 내에서 균등한 간격의 num개 숫자 배열 생성
* **`np.eye(N)`**: $N \times N$ 크기의 단위 행렬(우하향 대각선만 1이고 나머지는 0) 생성
* **`.size` / `.ndim` / `.shape`**: 원소의 수 / 차원값 / 행렬 확인</u>

---

## 2. 배열 형태 및 구조 변환 (Reshaping & Manipulation)

* **<u>`np.reshape(a, newshape)`**: 원소 수 유지하며 지정한 차원/모양으로 변경 / 인자가 -1이면 자동 계산을 의미
* **`np.triu(object)`**: 해당 행렬을 위쪽 삼각형 부분만 만기고 0으로 변환
* **`.T`**: 행과 열(축) 위치를 바꿈 (전치 행렬)
* **`np.newaxis`**: 새로운 축(차원)을 추가함</u>
* **`np.concatenate((a1, a2, ...), axis=0)`**: 지정한 축 기준으로 여러 배열 결합
* **`np.vstack(tup)` / `np.hstack(tup)`**: 수직(행) 또는 수평(열) 방향으로 배열 쌓기
* **`np.expand_dims(a, axis)`**: 지정한 축 위치에 차원 추가
* **`np.squeeze(a)`**: 크기가 1인 차원을 모두 제거
* **`ndarray.flatten()` / `ndarray.ravel()`**: 다차원 배열을 1차원으로 평평하게 펼침 (`flatten`은 복사본, `ravel`은 뷰 반환)

---

## 3. 조건 검색 및 정렬 (Searching & Sorting)

* **`np.where(condition[, x, y])`**: 조건 만족 시 `x`, 불만족 시 `y` 적용 (조건만 입력하면 충족 인덱스 튜플 반환)
* **`np.select(condlist, choicelist)`**: 다중 조건과 대응되는 값 리스트를 적용하여 원소 선택
* **<u>`np.sort(a)` / `ndarray.sort()`**: 배열 정렬 (`np.sort`는 새 배열 반환, `ndarray.sort`는 원본 정렬)</u>
* **`np.argsort(a)`**: 정렬되었을 때의 원래 인덱스 번호 배열 반환
* **`np.nonzero(a)`**: 0이 아닌 원소들의 인덱스 튜플 반환
* **`np.isin(element, test_elements)`**: 각 원소가 비교 대상에 포함되는지 여부(Bool 배열) 반환

---

## 4. 수학 및 통계 연산 (Math & Statistics)

* **<u>`np.sum(a)` / `np.mean(a)`**: 원소 전체 또는 특정 축(`axis`)의 합계 및 평균 구하기 (`axis=0`)은 열 /  (`axis=1`)은 행
* **`np.std(a)` / `np.var(a)`**: 표준편차 및 분산 계산
* **`np.min(a)` / `np.max(a)`**: 최솟값 및 최댓값 반환</u>
* **`np.argmin(a)` / `np.argmax(a)`**: 최솟값 / 최댓값이 위치한 인덱스 반환
* **<u>`np.abs(x)` / `np.sqrt(x)`**: 각 원소별 절댓값 및 제곱근 연산
* **`np.exp(x)` / `np.log(x)`**: 지수 함수 및 자연로그 연산</u>
* **`np.round(a, decimals=0)`**: 지정한 소수점 자릿수로 반올림
* **`np.clip(a, a_min, a_max)`**: 지정한 최소/최대 범위로 값 제한

---

## 5. 선형대수 및 집합 연산 (Linear Algebra & Set Operations)

* **<u>`np.dot(a, b)` / `a @ b`**: 두 배열의 행렬 곱(내적) 계산</u>
* **`np.linalg.inv(a)`**: 역행렬(Inverse Matrix) 계산
* **`np.unique(ar)`**: 중복 원소를 제거하고 정렬된 고유값 배열 반환

---

## 6. 난수 생성 (`np.random` 모듈)

* **<u>`np.random.rand(d0, d1, ...)`**: [0, 1) 범위의 균등 분포 난수 배열 생성</u>
* **`np.random.randn(d0, d1, ...)`**: 평균 0, 표준편차 1인 표준정규분포 난수 배열 생성
* **<u>`np.random.randint(low, high, size)`**: 지정 범위 내 정수 난수 배열 생성
* **`np.random.choice(a, size, replace)`**: 주어진 배열에서 무작위 샘플 추출</u>
* **`np.random.shuffle(x)` / `np.random.permutation(x)`**: 원소 순서를 무작위로 섞음 (`shuffle`은 원본 직접 변경, `permutation`은 새 배열 반환)
* **<u>`np.random.seed(seed)`**: 난수 생성 시드 고정 (실험 재현성 확보) - seed 값을 바꾸면 새로운 난수 생성</u>


---
---


# Pandas 주요 메서드 및 함수 정리
* 데이터 분석, 조작 - 데이터 정제, 필터링, 전처리용

## 1. 데이터 생성 및 입출력 (Data Creation & I/O)

* **<u>`pd.DataFrame(data)`**: 리스트, 딕셔너리, NumPy 배열 등을 2차원 데이터프레임으로 변환</u>
* **`pd.Series(data)`**: 1차원 시리즈 객체 생성
* **<u>`pd.read_csv(filepath)`**: CSV 파일을 데이터프레임으로 불러오기</u>
* **`pd.read_excel(filepath)`**: 엑셀 파일을 데이터프레임으로 불러오기
* **`pd.read_sql(sql, con)`**: SQL 쿼리 결과 또는 테이블을 데이터프레임으로 불러오기
* **`df.to_csv(filepath)`**: 데이터프레임을 CSV 파일로 저장
* **`df.to_excel(filepath)`**: 데이터프레임을 엑셀 파일로 저장

---

## 2. 데이터 확인 및 구조 탐색 (Exploration & Inspection)

* **<u>`df.head(n)` / `df.tail(n)`**: 상위 / 하위 `n`개 행 확인 (기본값 5)
* **`df.sample(n)`**: 무작위로 `n`개 행 샘플링
* **<u style="text-decoration: underline red 2px;">`df.info()`**: 데이터프레임의 행/열 개수, 컬럼명, 데이터 타입, 결측치 수 요약 출력
* **`df.describe()`**: 수치형 컬럼의 기술통계량(개수, 평균, 표준편차, 사분위수 등) 계산</u> 
* **`df.dtypes`**: 각 컬럼의 데이터 타입 반환 (속성)
* **`df.shape`**: 행과 열의 크기를 튜플 `(rows, cols)` 형태로 반환 (속성)
* **`df.columns` / `df.index`**: 컬럼명 목록 / 행 인덱스 정보 반환 (속성)
* **`df[s].value_counts()`**: 시리즈 내 [s]별 빈도수(개수) 계산
* **`df[s].nunique()` / `df[s].unique()`**: [s]의 개수 반환 / [s]의 배열 반환</u>

---

## 3. 데이터 선택 및 필터링 (Selection & Filtering)

* **`df['col']` / `df[['c1', 'c2']]`**: 단일 컬럼(Series) 또는 여러 컬럼(DataFrame) 선택
* **<u>`df.idxmax()` / `.idxmin()`**: 최댓값 / 최솟값을 가진 인덱스 반환  
* **`df.loc[(조건), (칼럼)]`**: 조건이 맞는 행의 해당 칼럼을 반환 / ex) df.loc[df["지역"] == "서울", "매출"] - 지역이 서울인 열의 매출만 보겠다
* **`df.iloc[row_idx, col_idx]`**: 정수 인덱스(위치) 기반 행/열 슬라이싱 및 선택 / 표를 좌표로 보고 인덱스값을 좌표값으로 해서 가져옴</u>
* **`df.query('condition')`**: 문자열 조건식을 사용한 간결한 데이터 필터링 (예: `df.query('age > 20')`)
* **<u>`df[s].isin(values)`**: 특정 값 리스트에 포함되는지 여부를 Bool 타입으로 반환 (조건 필터링에 활용)
* **`df[s].(dtype).contains(a)`**: [s]에서 (dtype)으로 (a)가 포함되어 있으면 반환  
* **`df[s].(dtype).startswith(a)`**: [s]에서 (dtype)으로 (a)로 시작하는 값을 반환  
* **`df.nlargest(n, colums)` / `df.nsmallest(n, colums)`**: 해당 칼럼 기준 상위 / 하위 n개 행 추출
* **`df.sort_values(colums, (ascending=T / F))`**: 해당 칼럼의 값을 기준으로 전체 정렬, ascending이 True면 오름차순 False면 내림차순 </u>
* **`s.between(left, right)`**: 지정한 범위 내에 값이 존재하는지 여부 반환

---

## 4. 데이터 정제 및 결측치/중복 처리 (Cleaning & Missing Data)

* **`df.isna()` / `df.isnull()`**: 결측치(NaN) 여부를 Bool 마스크로 반환
* **`df.notna()`**: 결측치가 아닌 정상 데이터 여부를 Bool 마스크로 반환
* **<u>`df.dropna(axis=0, subset='col', how='')`**: 결측치가 포함된 행/열 삭제 / subset='col' - 'col'에 해당하는 칼럼만 검사 / how='' - 여러 칼럼을 동시에 검사할 때 사용, 'any'라면 칼럼 중 하나라도 빈 값이면 삭제, 'all'이면 모든 칼럼이 빈 값이어야 삭제</u>
* **`df.fillna(value)`**: 결측치를 특정 값 또는 지정된 방식(앞/뒤 값 채우기)으로 대체
* **`df.duplicated()`**: 중복된 행 여부를 Bool 마스크로 반환
* **`df.drop_duplicates()`**: 중복된 행 제거
* **`df.replace(to_replace, value)`**: 특정 값을 다른 값으로 치환

---

## 5. 데이터 변환 및 수정 (Transformation & Modification)

* **`df.rename(columns={'old': 'new'})`**: 컬럼명 또는 인덱스 이름 변경
* **`s.astype(dtype)`**: 데이터 타입을 변환 (예: `'int64'`, `'float64'`, `'str'`, `'category'`)
* **`s.apply(func)` / `df.apply(func, axis=0)`**: 행/열 또는 시리즈에 사용자 정의 함수 적용
* **`s.map(dict_or_func)`**: 시리즈의 각 요소에 딕셔너리 매핑 또는 함수 적용
* **`df.map(func)`**: 데이터프레임 전체의 모든 원소에 함수 적용 (Pandas 2.1+ / 구 `applymap`)
* **<u>`df.drop(labels', axis=1)`**: 지정한 행 또는 열 삭제
* **`df.corr(numeric_only=True)`**: 칼럼들 간의 상관계수를 계산 / numeric_only=True - 문자열 등은 제외하고 숫자로 이루어진 칼럼들만 선택 / 상관계수 - 각 칼럼 간에 얼마나 밀첩한 상관관계가 있는지 -1부터 1까지의 수로 나타낸 것, 0에서 멀어질수록 상관도가 높음, 히트맵 그릴 때 자주 사용</u>
* **`df.sort_values(by='col', ascending=True)`**: 특정 컬럼 기준 값 정렬
* **`df.sort_index()`**: 인덱스 기준으로 정렬
* **`df.set_index('col')`**: 특정 컬럼을 행 인덱스로 지정
* **<u>`df.reset_index(drop=False)`**: 인덱스를 초기화하고 기본 정수 인덱스로 재설정 (그룹화해서 다중 인덱스가 들어갈 경우 사용) </u>

---

## 6. 데이터 결합 및 병합 (Combining & Merging)

* **`pd.concat([df1, df2], axis=0)`**: 데이터프레임을 수직(행) 또는 수평(열) 방향으로 단순 연결
* **`pd.merge(left, right, on='key', how='inner')`**: 공통 키 컬럼을 기준(SQL의 JOIN)으로 두 데이터프레임 병합 (`'inner'`, `'left'`, `'right'`, `'outer'`)
* **`df1.join(df2)`**: 행 인덱스를 기준으로 두 데이터프레임 결합

---

## 7. 그룹화 및 집계 (Grouping & Aggregation)

* **<u>`df.groupby('cols')['col'].(집계함수)()`**: 컬럼(들)을 기준으로 컬럼 1를 (집계함수)를 사용해 그룹화 / ex) df.groupby("지역")["매출"].sum - 지역별로 매출을 더한다. </u>/ (`DataFrameGroupBy` 객체 반환) 
* **`groupby.agg({'col1': 'sum', 'col2': 'mean'})`**: 그룹별로 여러 컬럼에 각각 다른 집계 함수 적용
* **`groupby.transform(func)`**: 그룹별 집계 결과를 원본과 동일한 크기의 원본 행 스케일로 반환
* **`groupby.filter(func)`**: 그룹 단위 조건 검사를 통과한 데이터만 필터링
* **`pd.pivot_table(df, values=..., index=..., columns=..., aggfunc='mean')`**: 피벗 테이블 작성
* **`pd.crosstab(index, columns)`**: 두 범주형 변수 간의 교차표(빈도 집계) 생성

---

## 8. 시계열 및 통계 연산 (Time Series & Rolling)

* **`pd.to_datetime(arg)`**: 문자열이나 숫자를 Datetime 객체(날짜/시간) 타입으로 변환
* **`s.dt` 접근자**: 날짜 타입에서 요소 추출 (`.dt.year`, `.dt.month`, `.dt.day`, `.dt.day_name()` 등)
* **`df.resample('M')`**: 시계열 데이터의 리샘플링 (일별 $
ightarrow$ 월별, 연도별 등 단위 변환 및 집계)
* **`s.shift(periods=1)`**: 데이터를 지정한 기간만큼 위/아래로 이동 (시차 변수 생성)
* **`s.pct_change()`**: 이전 항목 대비 변화율(증감률) 계산
* **`s.rolling(window=n)`**: 이동평균 등 구간 단위의 슬라이딩 윈도우 연산 수행


---
---


# Seaborn 주요 메서드 및 함수 정리
* 데이터 시각화 - 통계 그래프, 히트맵, 분포도 구현용 / Matplotlib과 역할 겹침

## 1. 관계형 그래프 (Relational Plots)

두 연속형 변수 간의 관계 또는 경향성을 시각화합니다.

* **`sns.relplot(data, x, y, kind='scatter'|'line', hue=...)`**: 관계형 그래프 통합 생성 함수 (FacetGrid 기반, 서브플롯 생성 용이)
* **<u>`sns.scatterplot(data, x, y, color=..., size=..., style=..., alpha=...)`**: 산점도(Scatter Plot) 생성 (색상 `color`, 크기 `size`, 모양 `style`, 투명도 `alpha`로 범주 구분)
* **`sns.lineplot(data, x, y, hue=..., errorbar=...)`**: 선 그래프(Line Plot) 생성 (데이터의 신뢰구간/오차범위 자동 계산 및 표시)</u>

---

## 2. 범주형 그래프 (Categorical Plots)

범주형 변수와 수치형 변수 간의 분포나 비교를 시각화합니다.

* **`sns.catplot(data, x, y, kind='box'|'bar'|..., hue=...)`**: 범주형 그래프 통합 생성 함수 (FacetGrid 기반)
* **`sns.barplot(data, x, y, hue=..., estimator='mean')`**: 평균값과 오차막대(Error bar)를 포함한 막대 그래프 작성
* **`sns.countplot(data, x=..., hue=...)`**: 각 범주별 데이터 개수(빈도) 수직/수평 막대 그래프 작성
* **`sns.boxplot(data, x, y, hue=...)`**: 상자 수염 그림(Box Plot) 작성 (이상치, 중앙값, 4분위수 시각화)
* **`sns.violinplot(data, x, y, hue=..., split=True)`**: 바이올린 형태로 데이터의 밀도 분포와 4분위수 동시 시각화
* **`sns.stripplot(data, x, y, jitter=True)`**: 범주별 개별 데이터 포인트를 점으로 흩뿌려 시각화
* **`sns.swarmplot(data, x, y)`**: 데이터 포인트가 겹치지 않도록 옆으로 펼쳐서 시각화
* **`sns.pointplot(data, x, y, hue=...)`**: 범주별 점과 점을 선으로 이어 변화 추이 강조 시각화

---

## 3. 분포 그래프 (Distribution Plots)

단일 변수 또는 두 변수 간의 데이터 분포 및 밀도를 시각화합니다.

* **`sns.displot(data, x, kind='hist'|'kde'|'ecdf')`**: 분포 그래프 통합 생성 함수
* **<u>`sns.histplot(data, x, kde=True, bins=(n), color= ...)`**: 히스토그램(막대 그래프) 생성 / kde=True - 밀도 추정선(선그래프) 표시  / bins=(n) - 전체 범위를 n개의 구간(막대)로 나누어 집계 </u>
* **`sns.kdeplot(data, x, fill=True)`**: 커널 밀도 추정(Kernel Density Estimation) 곡선 시각화
* **`sns.ecdfplot(data, x)`**: 누적 분포 함수(ECDF) 곡선 시각화
* **`sns.rugplot(data, x)`**: 축 상에 개별 데이터 위치를 작은 틱(선)으로 표시

---

## 4. 회귀 및 통계 모델링 그래프 (Regression Plots)

변수 간 선형 관계 및 회귀 모델 추정선을 시각화합니다.

* **<u>`sns.regplot(data, x, y, ci=95)`**: 산점도와 함께 선형 회귀선 및 신뢰구간(ci) 작성</u>
* **`sns.lmplot(data, x, y, hue=..., col=..., row=...)`**: `regplot`과 `FacetGrid`를 결합하여 범주별 회귀선 다중 서브플롯 시각화
* **`sns.residplot(data, x, y)`**: 회귀 모델 잔차(Residuals) 분포 그래프 시각화

---

## 5. 다중 그리드 및 행렬 그래프 (Matrix & Multi-plot Grids)

데이터프레임 전체 또는 여러 변수 간의 관계/상관관계를 다중 패널 형태로 시각화합니다.

* **<u>`sns.heatmap(data, mask=mask, annot=True, cmap='coolwarm', fmt='.(n)f', linewidths=(n))`**: 2차원 행렬(상관계수 등) 데이터의 히트맵 시각화 / mask=mask - 앞의 mask는 매개변수 이름으로 True인 부분을 빈칸으로 놔두고 False인 부분만 매개변수와 색상으로 채움, 뒤의 mask는 True, False로 구성된 배열  / annot=True - 각 칸에 숫자들을 직접 표기할지 여부 / cmap='coolwarm' - 색산 테마 /  </u>
* **`sns.clustermap(data, cmap=...)`**: 계층적 클러스터링(Hierarchical Clustering)을 수행한 히트맵 및 덴드로그램 시각화
* **<u>`sns.pairplot(data, corner=True, kind="reg")`**: 각 칼럼 간의 관계를 모두 그래프화 해서 보여줌 / corner=True - 대각선 아래만 보여줌(mask와 같은 원리) / kind="reg" - 산점도 위에 선형 회귀선을 그어줌 </u>
* **`sns.jointplot(data, x, y, kind='scatter'|'kde'|'hex'|'reg')`**: 두 변수의 관계 그래프와 각 변수의 단변량 분포 그래프를 축 가장자리에 결합하여 시각화 / fmt='.(n)f' - 소숫점 n 번째 자리까지 표시, "d"를 넣으면 정수만 표시 / linewidths=(n) - 칸 사이에 n 픽셀 두께의 하얀 구분선을 넣음 

---

## 6. 테마, 색상 팔레트 및 설정 (Themes & Palettes)

* **`sns.set_theme(style='darkgrid'|'whitegrid'|'ticks', palette=...)`**: Seaborn 전체 그래프 스타일 및 테마 일괄 설정
* **`sns.set_style('whitegrid')`**: 배경 격자 스타일 설정
* **`sns.set_palette('pastel'|'husl'|'Set2')`**: 기본 색상 팔레트 설정
* **`sns.color_palette()`**: 현재 또는 지정한 팔레트의 RGB 색상 리스트 반환 / 확인
* **<u style="text-decoration: underline red 2px;">`sns.load_dataset('dataset_name')`**: Seaborn 온라인 예제 데이터셋(예: `'iris'`, `'titanic'`, `'tips'`) 불러오기</u>


---
---


# Matplotlib 주요 메서드 및 함수 정리
* 데이터 시각화 - 차트, 그래프 작성 및 커스터마이징 / Seaborn과 역할 겹침

## 1. 캔버스 및 서브플롯 생성 (Figure & Axes Creation)

* **<u>`plt.figure(figsize=(w, h), dpi=...)`**: 앞으로 그리려는 그래프의 크기/해상도 지정 - w, h 값</u>
* **`plt.subplots(nrows, ncols)`**: 여러 개의 그래프(Axes)를 격자 형태로 동시에 생성 (Figure와 Axes 배열 반환)
* **`plt.subplot(nrows, ncols, index)`**: 격자 영역 중 특정 위치의 단일 서브플롯 지정
* **`fig.add_subplot()`**: Figure 객체에 새로운 서브플롯 추가
* **`plt.tight_layout()`**: 그래프 간 간격과 레이블이 겹치지 않도록 여백 자동 조절

---

## 2. 기본 차트 유형별 그리기 (Basic Plotting)

* **<u>`plt.plot(x, y, color=..., linestyle=..., marker=...)`**: 선 그래프(Line Plot) 작성
* **`plt.scatter(x, y, s=..., c=..., alpha=...)`**: 산점도(Scatter Plot) 작성 (점 크기 및 색상 지정 가능)</u>
* **`plt.bar(x, height)` / `plt.barh(y, width)`**: 수직 / 수평 막대 그래프(Bar Chart) 작성
* **`plt.hist(x, bins=...)`**: 히스토그램(Histogram) 작성 (구간 수 지정 가능)
* **`plt.boxplot(x)`**: 상자 수염 그림(Box Plot) 작성 (이상치 및 사분위수 확인)
* **`plt.pie(x, labels=..., autopct=...)`**: 파이 차트(Pie Chart) 작성 (비율 표시 가능)
* **`plt.imshow(X, cmap=...)`**: 2D 이미지 또는 행렬 데이터를 히트맵 형태로 표시

---

## 3. 축, 제목 및 레이블 설정 (Axes & Labels)

* **<u>`plt.title('title')` / `ax.set_title('title')`**: 그래프 제목 설정
* **`plt.xlabel('text')` / `plt.ylabel('text')`**: X축 / Y축 레이블 이름 설정</u>
* **`plt.xlim(min, max)` / `plt.ylim(min, max)`**: X축 / Y축 범위(한계값) 지정
* **`plt.xticks(ticks, labels)` / `plt.yticks(ticks, labels)`**: X축 / Y축 눈금 위치 및 표시 문구 설정
* **`plt.axis('equal' | 'off')`**: 축 비율을 동일하게 고정하거나 축 전체를 숨김

---

## 4. 스타일, 범례 및 주석 추가 (Styling, Legend & Annotation)

* **<u>`plt.legend(loc='best')`**: 범례(Legend) 표시 및 위치 지정 / 기본값은 자동 배치 - 데이터들을 가장 덜 가리는 곳
* **`plt.grid(True, linestyle=...)`**: 그래프 격자선(Grid) 표시 여부 설정</u>
* **`plt.axhline(y=0)` / `plt.axvline(x=0)`**: 수평선 / 수직선 추가 (기준선 표시용)
* **`plt.axhspan()` / `plt.axvspan()`**: 특정 수평 / 수직 구간에 배경색 칠하기
* **`plt.text(x, y, 'text')`**: 지정한 좌표에 텍스트 주석 추가
* **`plt.annotate('text', xy=(x, y), xytext=..., arrowprops=...)`**: 화살표가 포함된 상세 주석 추가
* **`plt.style.use('style_name')`**: 그래프 전체 테마 스타일 적용 (예: `'ggplot'`, `'seaborn-v0_8'`)

---

## 5. 출력 및 저장 (Output & File Saving)

* **<u>`plt.show()`**: 생성한 그래프를 화면에 출력 - 사실 안 써도 출력은 해주는데, 쓰면 깔끔하게 출력</u>
* **`plt.savefig('filename.png', dpi=300, bbox_inches='tight')`**: 그래프를 이미지 파일(PNG, PDF 등)로 저장
* **`plt.clf()` / `plt.cla()`**: 현재 Figure의 모든 내용 삭제 / 현재 Axes의 내용 삭제
* **`plt.close()`**: 생성된 Figure 창을 닫고 메모리 해제


---
---


# Scikit-Learn 주요 메서드 및 클래스 정리 (단계별/기능별)
* 전처리부터 머신러닝 모델 구축 및 평가까지의 전 과정 구현 - 싸이킷 런은 머신러닝 특화 / 파이토치는 딥러닝 특화

## 1. 데이터 전처리 및 변환 (Data Preprocessing & Feature Engineering)

데이터 표준화, 인코딩, 결측치 처리 등을 수행합니다.

* **<u>`StandardScaler()`**: 데이터의 평균을 0, 표준편차를 1로 변환하는 표준화(Standardization) 수행</u>
* **<u>`fit(x)`**: 데이터 x의 평균과 표준편차를 구해서 저장 / 인자를 2개 넣으면 회귀 함수 찾기용</u>
* **`MinMaxScaler()`**: 데이터를 지정한 범위(기본값 [0, 1]) 내로 압축하는 정규화(Normalization) 수행
* **`RobustScaler()`**: 중앙값과 IQR(사분위수 범위)을 활용해 이상치(Outlier)에 강건한 스케일링 수행
* **`LabelEncoder()`**: 범주형 타겟 레이블을 정수형 숫자로 변환 (`fit_transform()`, `inverse_transform()`)
* **`OneHotEncoder()`**: 범주형 특성을 더미 변수(One-Hot Vector)로 변환
* **`SimpleImputer(strategy='mean')`**: 결측치(NaN)를 평균, 중앙값, 최빈값 등으로 대체
* **`PolynomialFeatures(degree=2)`**: 다항식 및 교차작용 특성을 생성하여 차원 확장

---

## 2. 데이터 분할 및 교차 검증 (Data Splitting & Cross-Validation)

학습용 및 검증용 데이터를 분할하고 모델 평가 프레임을 제공합니다.

* **`train_test_split(X, y, test_size=0.2, stratify=y)`**: 데이터를 학습용/평가용 세트로 분할
* **`KFold(n_splits=5, shuffle=True)`**: 데이터셋을 K개로 나누어 교차 검증 수행
* **`StratifiedKFold(n_splits=5)`**: 클래스 비율을 유지하며 K-겹 교차 검증 수행 (불균형 데이터용)
* **`cross_val_score(estimator, X, y, cv=5)`**: 지정한 모델 및 교차 검증 기준에 맞춰 평가 점수 리스트 반환

---

## 3. 슈퍼바이저 알고리즘 (Supervised Learning Algorithms)

### 3.1 회귀 모델 (Regression)
* **<u style="text-decoration: underline red 2px;">`.fit(x, y)`**: x, y로 학습해 정규방정식을 이용해 최적의 함수 방정식을 찾아줌 / 인자를 하나만 넣으면 전처리용</u>
* **<u>`.predict()`**: fit로 찾은 최적의 패턴에 ()의 값을 대입하여 결과를 도출 / ex) y_hat = model.predict(X)</u>

* **`LinearRegression()`**: 기본 선형 회귀 알고리즘
* **`Ridge(alpha=1.0)`**: L2 규제(Regularization)가 적용된 선형 회귀
* **`Lasso(alpha=1.0)`**: L1 규제가 적용되어 불필요한 특성을 0으로 만드는 회귀

### 3.2 분류 모델 (Classification)
* **<u>`.predict_proba()`**: 예측 결과가 아니라 예측 확률값을 반환 </u>
* **`LogisticRegression()`**: 로지스틱 회귀 기반 이진/다중 분류 모델
* **`KNeighborsClassifier(n_neighbors=5)`**: K-최근접 이웃 알고리즘 기반 분류기
* **`SVC(kernel='rbf', C=1.0)`**: 서포트 벡터 머신(SVM) 분류기

### 3.3 트리 및 앙상블 모델 (Trees & Ensembles)
* **`DecisionTreeClassifier()` / `DecisionTreeRegressor()`**: 의사결정나무 모델
* **`RandomForestClassifier()` / `RandomForestRegressor()`**: 배깅(Bagging) 기반 랜덤 포레스트 앙상블
* **`GradientBoostingClassifier()` / `GradientBoostingRegressor()`**: 그래디언트 부스팅(GBM) 앙상블
* **`VotingClassifier(estimators=[...])`**: 여러 모델의 예측을 투표 방식으로 결합하는 보팅 앙상블

### predict의 사용 
* 모델의 종류에 따라 반환되는 값의 형태가 달라짐
* 회귀 모델 : 연속된 수치(숫자)를 반환 (예: 식사 금액에 따른 예상 팁 금액)
* 분류 모델 : 데이터가 속할 클래스(범주/라벨)를 반환 (예: 0 또는 1, '합격' 또는 '불합격')
* &emsp;predict_proba는 확률을 반환
---

## 4. 비지도 학습 및 차원 축소 (Unsupervised Learning & Dimensionality Reduction)

군집화(Clustering) 및 데이터 차원 축소를 수행합니다.

* **`KMeans(n_clusters=3)`**: K-평균 군집화 알고리즘
* **`DBSCAN(eps=0.5, min_samples=5)`**: 밀도 기반 군집화 알고리즘 (이상치 탐지 가능)
* **`PCA(n_components=2)`**: 주성분 분석을 통한 차원 축소 (분산 보존)
* **`TSNE(n_components=2)`**: 고차원 데이터를 2/3차원으로 시각화하기 위한 차원 축소

---

## 5. 하이퍼파라미터 튜닝 및 파이프라인 (Hyperparameter Tuning & Pipeline)

모델 최적화 및 작업 흐름 관리 도구입니다.

* **`GridSearchCV(estimator, param_grid, cv=5)`**: 지정한 파라미터 조합을 전수 조사하여 최적 파라미터탐색
* **`RandomizedSearchCV(estimator, param_distributions, n_iter=10)`**: 지정 범위 내 파라미터를 무작위로 추출하여 탐색
* **`Pipeline([('scaler', StandardScaler()), ('model', Ridge())])`**: 전처리-모델링 과정을 단일 객체로 연결하여 워크플로우 캡슐화
* **`make_pipeline()`**: 이름 지정 없이 객체 순서대로 간단하게 파이프라인 생성

---

## 6. 모델 평가 지표 (Evaluation Metrics - `sklearn.metrics`)

예측 성능을 정량적으로 측정합니다.

### 6.1 회귀 평가 지표
* **`mean_squared_error(y_true, y_pred)`**: 평균 제곱 오차 (MSE) 계산
* **`mean_absolute_error(y_true, y_pred)`**: 평균 절대 오차 (MAE) 계산
* **`r2_score(y_true, y_pred)`**: 결정 계수 ($R^2$ Score) 계산

### 6.2 분류 평가 지표
* **`accuracy_score(y_true, y_pred)`**: 정확도(Accuracy) 측정
* **`precision_score()` / `recall_score()` / `f1_score()`**: 정밀도, 재현율, F1-점수 측정
* **`confusion_matrix(y_true, y_pred)`**: 혼동 행렬(Confusion Matrix) 생성
* **`classification_report(y_true, y_pred)`**: 주요 분류 지표 일괄 리포트 출력
* **`roc_auc_score(y_true, y_score)`**: ROC 곡선의 밑면적(AUC) 점수 계산


---
---


# PyTorch 주요 모듈 및 메서드 정리 (단계별/기능별)
* 딥러닝 및 인공지능 모델 개발 - 싸이킷 런은 머신러닝 특화 / 파이토치는 딥러닝 특화 / 활용법은 Numpy와 차부뚜어

## 1. 텐서 생성 및 기본 연산 (Tensor Creation & Operations)

PyTorch의 기본 데이터 구조인 텐서(Tensor)를 생성하고 가공합니다.

* **<u>`torch.tensor(data)`**: 파이썬 리스트나 NumPy 배열로부터 텐서 생성 - CPU 뿐만 아니라 GPU로도 계산 가능한 배열</u>
* **`torch.zeros(shape)` / `torch.ones(shape)`**: 0 또는 1로 채워진 텐서 생성
* **`torch.arange(start, end, step)`**: 연속된 숫자로 구성된 텐서 생성
* **`torch.from_numpy(ndarray)`**: NumPy 배열을 텐서로 변환 (메모리 공유)
* **`tensor.numpy()`**: PyTorch 텐서를 NumPy 배열로 변환
* **`tensor.to(device)`**: 텐서를 연산 장치(`'cpu'` 또는 `'cuda'`)로 이동
* **`tensor.reshape(*shape)` / `tensor.view(*shape)`**: 텐서의 형태(Shape) 변경 (`view`는 메모리 연속성 요구)
* **`tensor.squeeze()` / `tensor.unsqueeze(dim)`**: 크기가 1인 차원 제거 또는 특정 위치에 차원 추가
* **`torch.cat(tensors, dim=0)`**: 지정한 차원을 기준으로 여러 텐서 결합

---

## 2. 데이터 처리 및 로더 (Data Loading & Preprocessing - `torch.utils.data`)

대용량 데이터를 효율적으로 관리하고 학습에 배치 단위로 공급합니다.

* **`Dataset`**: 커스텀 데이터셋을 정의하기 위한 기본 클래스 (`__len__`, `__getitem__` 구현)
* **`TensorDataset(*tensors)`**: 여러 텐서(입력 X, 타겟 y)를 하나로 묶어주는 기본 데이터셋
* **`DataLoader(dataset, batch_size=32, shuffle=True)`**: 배치 생성, 데이터 셔플, 다중 프로세스 로딩을 자동화

---

## 3. 신경망 구축 모듈 (Neural Network Building - `torch.nn`)

딥러닝 모델 레이어를 구성하는 핵심 클래스입니다.

* **`nn.Module`**: 모든 신경망 모델의 기본 클래스 (`__init__`에서 레이어 정의, `forward()`에서 순전파 정의)
* **<u>`nn.Sequential(*args)`**: 레이어를 순차적으로 엮어 직관적으로 신경망 구성
* **`nn.Linear(in_features, out_features)`**: 입력 데이터를 기반으로 기본적인 선형 방정식 생성 / in_features - 입력 변수의 개수 / out_features - 출력 변수의 개수 </u>
* **`nn.Conv2d(in_channels, out_channels, kernel_size)`**: 2차원 합성곱(Convolutional) 레이어 (이미지 처리)
* **`nn.MaxPool2d(kernel_size)` / `nn.AvgPool2d(kernel_size)`**: 2차원 풀링 레이어
* **`nn.Dropout(p=0.5)`**: 과적합 방지를 위한 드롭아웃 레이어
* **`nn.BatchNorm2d(num_features)`**: 배치 정규화(Batch Normalization) 레이어
* **<u>`nn.Sigmoid()`**: 출력값을 0~1 사이로 제한 / 합격, 불합격의 확률을 계산 가능 </u>
* **`nn.ReLU()` / `nn.Sigmoid()` / `nn.Softmax(dim=1)`**: 활성화 함수(Activation Functions)

---

## 4. 손실 함수 (Loss Functions - `torch.nn`)

모델의 예측값과 실제 정답 사이의 오차를 측정합니다.

* **<u>`nn.MSELoss()`**: MSE 구하기 </u>
* **`nn.CrossEntropyLoss()`**: 다중 클래스 분류(Classification)용 손실 함수 (Softmax 내장)
* **`nn.BCEWithLogitsLoss()`**: 이진 분류(Binary Classification)용 손실 함수 (Sigmoid 내장)

---

## 5. 최적화 알고리즘 (Optimization - `torch.optim`)

역전파를 통해 구한 경사(Gradient)로 모델 파라미터(가중치)를 업데이트합니다.

* **<u>`optim.SGD(model.parameters(), lr=0.01)`**: 확률적 경사 하강법(GD) 최적화 / model.parameters() - `nn.Linear`에서 만든 함수의 학습 가능한 모든 파라미터를 사용하여 업데이트
* **`optim.Adam(model.parameters(), lr=0.001)`**: Adam 최적화</u>
* **`optim.AdamW(model.parameters(), lr=0.001)`**: Adam에 가중치 감쇠(Weight Decay)를 정확히 적용한 변형 (LLM/트랜스포머에 자주 사용)
* **<u>`optimizer.zero_grad()`**: 이전 단계에서 누적된 파라미터의 경사도(Gradient) 초기화</u>
* **`optimizer.step()`**: 계산된 경사도를 기반으로 모델 파라미터 업데이트

---

## 6. 자동 미분 및 학습 흐름 제어 (Autograd & Training Loop)

모델 학습 및 평가의 루프 과정 제어 도구입니다.

* **<u style="text-decoration: underline red 2px;">`.backward()`**: 미분 계산(함수의 경사도 계산) </u>
* **<u>`torch.no_grad()`**: 미분 추적 OFF - 자원 절약, 중간 평가나 최종 평가 때 
* **`model.train()`**: 모델을 학습 모드로 전환 (Dropout, BatchNorm 등의 동작 활성화)
* **`model.eval()`**: 모델을 평가 모드로 전환 (Dropout, BatchNorm 등의 동작 고정)
* **`torch.save(model.state_dict(), 'path.pth')`**: 모델의 가중치(파라미터) 저장
* **`model.load_state_dict(torch.load('path.pth'))`**: 저장된 가중치를 모델에 불러오기

---
---

# Hugging Face 핵심 모듈 및 함수 정리 (핵심 가이드)
* AI 모델, 데이터셋, 스페이스 등을 파이썬 코드로 제어하고 관리하는 라이브러리 

## 1. 파이프라인 & 모델 로딩 (`transformers`)

가장 기본적이고 자주 쓰이는 모델 구축 및 실행 함수입니다.

* **`pipeline(task, model=...)`**: 번역, 감정분석, 텍스트 생성 등 AI 작업을 한 줄 코드로 바로 실행
* **`AutoTokenizer.from_pretrained(model_id)`**: 텍스트를 모델 입력용 토큰(숫자)으로 변환하는 토크나이저 로드
* **`AutoModel.from_pretrained(model_id)`**: 사전 학습된 기본 모델 가중치 로드
* **`AutoModelForCausalLM.from_pretrained(...)`**: 텍스트 생성(LLM) 전용 모델 로드
* **`AutoModelForSequenceClassification.from_pretrained(...)`**: 텍스트 분류 전용 모델 로드

---

## 2. 데이터셋 관리 (`datasets`)

허깅페이스 허브의 공개 데이터셋을 불러오고 전처리합니다.

* **`load_dataset(path, name)`**: 허브에 올려진 데이터셋을 곧바로 로드
* **`dataset.map(function)`**: 데이터셋 전체에 토큰화 등 전처리 함수를 일괄 적용

---

## 3. 모델 학습 및 파인튜닝 (`transformers`)

가져온 사전 학습 모델을 내 데이터셋으로 재학습(Fine-tuning)시킵니다.

* **`TrainingArguments(output_dir, num_train_epochs, lr, ...)`**: 학습율, 배치 크기 등 학습 하이퍼파라미터 설정
* **`Trainer(model, args, train_dataset, eval_dataset, ...)`**: 학습/평가 루프를 자동으로 처리해주는 고성능 학습기

---

## 4. 허브 및 API 연동 (`huggingface_hub`)

허깅페이스 클라우드 서비스와 계정을 연동합니다.

* **`login(token=...)` / `notebook_login()`**: 비공개 모델 접근 및 내 모델 업로드를 위한 API 토큰 인증
* **`InferenceClient(model=...)`**: 모델을 다운로드하지 않고 클라우드 API를 호출해 빠른 예측 수행

---
---

# Transformers 주요 모듈 및 클래스 정리 (기능별)
* 사전 학습 AI 모델을 다룰 수 있는 라이브러리 

## 1. 파이프라인 및 고수준 추론 (Pipeline & High-Level Inference)

* **`pipeline(task, model=...)`**: 번역, 요약, 텍스트 생성, 감정 분석 등 다양한 AI 작업을 단 한 줄로 수행하는 고수준 API

---

## 2. 자동 클래스 및 로더 (AutoClasses & Model Loaders)

* **`AutoTokenizer.from_pretrained(model_id)`**: 모델 이름만으로 호환되는 토크나이저 자동 로드
* **`AutoModel.from_pretrained(model_id)`**: 기본 뼈대(Backbone) 사전 학습 모델 로드
* **`AutoModelForCausalLM.from_pretrained(model_id)`**: 텍스트 생성(LLM) 전용 인과적 언어 모델 로드
* **`AutoModelForSequenceClassification.from_pretrained(model_id)`**: 텍스트 분류 전용 모델 로드
* **`AutoConfig.from_pretrained(model_id)`**: 모델의 구조 및 하이퍼파라미터 설정 정보(Config) 로드

---

## 3. 토크나이저 및 텍스트 전처리 (Tokenizer & Preprocessing)

* **`tokenizer(text, padding=True, truncation=True, return_tensors='pt')`**: 텍스트를 모델 입력 형태(텐서)로 변환
* **`tokenizer.decode(token_ids)`**: 토큰 ID(숫자)를 사람이 읽을 수 있는 텍스트로 복원
* **`tokenizer.batch_decode(sequences)`**: 배치 형태의 여러 토큰 ID 리스트를 텍스트로 일괄 복원

---

## 4. 텍스트 생성 및 추론 제어 (Generation Options)

* **`model.generate(input_ids, max_new_tokens=..., temperature=...)`**: LLM 텍스트 생성 제어 (생성 길이, 무작위성 등 설정)
* **`DataCollatorWithPadding(tokenizer)`**: 배치 단위로 데이터 패딩을 동적으로 적용하는 데이터 컬레이터

---

## 5. 모델 파인튜닝 및 학습 (Fine-Tuning & Trainer)

* **`TrainingArguments(output_dir, learning_rate, num_train_epochs, ...)`**: 학습율, 배치 크기 등 학습용 설정 정의
* **`Trainer(model, args, train_dataset, eval_dataset, ...)`**: PyTorch 학습/평가 루프를 자동화하는 고성능 래퍼 클래스

---

## 6. 경량화 및 양자화 설정 (Quantization Configuration)

* **`BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=...)`**: 4비트/8비트 양자화를 이용해 적은 GPU 메모리로 대형 모델 로드 설정

<div>