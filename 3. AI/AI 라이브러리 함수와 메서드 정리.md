<div style="line-height: 2.5; font-size: 1.2em;">

# NumPy 주요 메서드 및 함수 정리 (기능별)
* 고성능 계산기 - 벡터, 행렬 계산용

## 1. 배열 생성 및 초기화 (Array Creation & Initialization)

* **<u>`np.array(object)`**: 파이썬 리스트/튜플 등을 NumPy 배열(`ndarray`)로 변환
* **`np.zeros(shape)`**: 모든 원소가 0인 배열 생성
* **`np.ones(shape)`**: 모든 원소가 1인 배열 생성
* **`np.full(shape, fill_value)`**: 지정한 특정 값으로 채워진 배열 생성
* **`np.arange([start,] stop[, step])`**: 지정한 범위와 간격의 연속된 숫자 배열 생성
* **`np.linspace(start, stop, num)`**: 지정한 범위 내에서 균등한 간격의 $N$개 숫자 배열 생성
* **`np.eye(N)`**: $N \times N$ 크기의 단위 행렬(Identity Matrix) 생성</u>

---

## 2. 배열 형태 및 구조 변환 (Reshaping & Manipulation)

* **<u>`np.reshape(a, newshape)`**: 원소 수 유지하며 지정한 차원/모양으로 변경 / 인자가 -1이면 자동 계산을 의미
* **`ndarray.T`**: 행과 열(축) 위치를 바꿈 (전치 행렬)
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
* **<u>`np.random.seed(seed)`**: 난수 생성 시드 고정 (실험 재현성 확보)</u>


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
* **`df.info()`**: 데이터프레임의 행/열 개수, 컬럼명, 데이터 타입, 결측치 수 요약 출력
* **`df.describe()`**: 수치형 컬럼의 기술통계량(개수, 평균, 표준편차, 사분위수 등) 계산 
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
* **<u>`df.dropna(axis=0, how='any')`**: 결측치가 포함된 행/열 삭제</u>
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
* **<u>`df.drop(labels', axis=1)`**: 지정한 행 또는 열 삭제</u>
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
* **`sns.histplot(data, x, kde=True, bins=...)`**: 히스토그램 생성 (밀도추정선 `kde=True` 옵션 지원)
* **`sns.kdeplot(data, x, fill=True)`**: 커널 밀도 추정(Kernel Density Estimation) 곡선 시각화
* **`sns.ecdfplot(data, x)`**: 누적 분포 함수(ECDF) 곡선 시각화
* **`sns.rugplot(data, x)`**: 축 상에 개별 데이터 위치를 작은 틱(선)으로 표시

---

## 4. 회귀 및 통계 모델링 그래프 (Regression Plots)

변수 간 선형 관계 및 회귀 모델 추정선을 시각화합니다.

* **<u>`sns.regplot(data, x, y, ci=95)`**: 산점도와 함께 선형 회귀선 및 신뢰구간(Confidence Interval) 작성</u>
* **`sns.lmplot(data, x, y, hue=..., col=..., row=...)`**: `regplot`과 `FacetGrid`를 결합하여 범주별 회귀선 다중 서브플롯 시각화
* **`sns.residplot(data, x, y)`**: 회귀 모델 잔차(Residuals) 분포 그래프 시각화

---

## 5. 다중 그리드 및 행렬 그래프 (Matrix & Multi-plot Grids)

데이터프레임 전체 또는 여러 변수 간의 관계/상관관계를 다중 패널 형태로 시각화합니다.

* **`sns.heatmap(data, annot=True, cmap='coolwarm', fmt='.2f')`**: 2차원 행렬(상관계수 등) 데이터의 히트맵 시각화
* **`sns.clustermap(data, cmap=...)`**: 계층적 클러스터링(Hierarchical Clustering)을 수행한 히트맵 및 덴드로그램 시각화
* **`sns.pairplot(data, hue=..., corner=True)`**: 데이터프레임 내 모든 수치형 변수 간의 쌍별(Pairwise) 관계 그래프 격자 작성
* **`sns.jointplot(data, x, y, kind='scatter'|'kde'|'hex'|'reg')`**: 두 변수의 관계 그래프와 각 변수의 단변량 분포 그래프를 축 가장자리에 결합하여 시각화

---

## 6. 테마, 색상 팔레트 및 설정 (Themes & Palettes)

* **`sns.set_theme(style='darkgrid'|'whitegrid'|'ticks', palette=...)`**: Seaborn 전체 그래프 스타일 및 테마 일괄 설정
* **`sns.set_style('whitegrid')`**: 배경 격자 스타일 설정
* **`sns.set_palette('pastel'|'husl'|'Set2')`**: 기본 색상 팔레트 설정
* **`sns.color_palette()`**: 현재 또는 지정한 팔레트의 RGB 색상 리스트 반환 / 확인
* **<u>`sns.load_dataset('dataset_name')`**: Seaborn 온라인 예제 데이터셋(예: `'iris'`, `'titanic'`, `'tips'`) 불러오기</u>

---
---



# Matplotlib 주요 메서드 및 함수 정리
* 데이터 시각화 - 차트, 그래프 작성 및 커스터마이징 / Seaborn과 역할 겹침

## 1. 캔버스 및 서브플롯 생성 (Figure & Axes Creation)

* **`plt.figure(figsize=(w, h), dpi=...)`**: 새로운 차트 캔버스(Figure) 객체 생성 및 크기/해상도 지정
* **`plt.subplots(nrows, ncols)`**: 여러 개의 그래프(Axes)를 격자 형태로 동시에 생성 (Figure와 Axes 배열 반환)
* **`plt.subplot(nrows, ncols, index)`**: 격자 영역 중 특정 위치의 단일 서브플롯 지정
* **`fig.add_subplot()`**: Figure 객체에 새로운 서브플롯 추가
* **`plt.tight_layout()`**: 그래프 간 간격과 레이블이 겹치지 않도록 여백 자동 조절

---

## 2. 기본 차트 유형별 그리기 (Basic Plotting)

* **<u>`plt.plot(x, y, color=..., linestyle=..., marker=...)`**: 선 그래프(Line Plot) 작성</u>
* **`plt.scatter(x, y, s=..., c=..., alpha=...)`**: 산점도(Scatter Plot) 작성 (점 크기 및 색상 지정 가능)
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

* **`plt.legend(loc='best')`**: 범례(Legend) 표시 및 위치 지정
* **`plt.grid(True, linestyle=...)`**: 그래프 격자선(Grid) 표시 여부 설정
* **`plt.axhline(y=0)` / `plt.axvline(x=0)`**: 수평선 / 수직선 추가 (기준선 표시용)
* **`plt.axhspan()` / `plt.axvspan()`**: 특정 수평 / 수직 구간에 배경색 칠하기
* **`plt.text(x, y, 'text')`**: 지정한 좌표에 텍스트 주석 추가
* **`plt.annotate('text', xy=(x, y), xytext=..., arrowprops=...)`**: 화살표가 포함된 상세 주석 추가
* **`plt.style.use('style_name')`**: 그래프 전체 테마 스타일 적용 (예: `'ggplot'`, `'seaborn-v0_8'`)

---

## 5. 출력 및 저장 (Output & File Saving)

* **`plt.show()`**: 생성한 그래프를 화면에 출력 (스크립트 실행 시 팝업 또는 출력창 표출)
* **`plt.savefig('filename.png', dpi=300, bbox_inches='tight')`**: 그래프를 이미지 파일(PNG, PDF 등)로 저장
* **`plt.clf()` / `plt.cla()`**: 현재 Figure의 모든 내용 삭제 / 현재 Axes의 내용 삭제
* **`plt.close()`**: 생성된 Figure 창을 닫고 메모리 해제

<div>