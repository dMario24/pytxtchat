import os
import pandas as pd
import termplotlib as tpl
from tabulate import tabulate

def get_parquet_path(dname='movies', isprint='True') -> str:
    """parquet 파일 경로를 반환

    Args:
        dname (str, optional): 데이터 종류 (movies, moviedetail 등). 기본값은 'movies'.
        isprint (str, optional): 경로를 출력할지 여부. 기본값은 True.

    Returns:
        str: parquet 파일의 절대 경로

    이 함수는 주어진 데이터 종류에 해당하는 파라쿼 파일의 절대 경로를 생성하고,
    isprint 가 True일 경우 경로를 출력합니다.
    """
    parquet_path = os.path.join(os.path.dirname(__file__), dname, f"{dname}.parquet")
    if isprint.lower() == 'true':
       print(parquet_path)
    return parquet_path


def get_dataframe(dname='movies') -> pd.DataFrame:
    """parquet 파일 경로를 반환

    Args:
        dname (str, optional): 데이터 종류 (movies, moviedetail 등). 기본값은 'movies'

    Returns:
        DataFrame: pandas dataframe

    이 함수는 주어진 데이터 종류에 해당하는 pandas dataframe 을 반환합니다.
    """
    p = get_parquet_path(dname=dname, isprint='False')
    df = pd.read_parquet(p)
    return df


def search_movie(word: str, column='movieNm', isprint='True', tablefmt='github'):
    """영화 검색 함수

    Args:
      word: 검색할 단어
      column: 검색할 컬럼 (기본값: 'movieNm') nationAlt, genreAlt, typeNm, directorNm, companyNm
      isprint: 검색 결과를 출력할지 여부 (기본값: 'True')
      tablefmt: 출력 형식 (기본값: 'github') plain, simple, grid, pipe, pretty, tsv ... https://pypi.org/project/tabulate/

    Returns:
      검색 결과를 담은 문자열 (테이블 형식)
    """
    df = get_dataframe()
    s = df[df[column].str.contains(word, na=False)]
    cols = ['movieNm', 'openDt', 'nationAlt', 'genreAlt', 'typeNm', 'directorNm', 'companyNm', 'movieCd', 'year']
    r = s[cols].sort_values(by=['movieNm', 'openDt'], ascending=[True, True])
    t = tabulate(r, headers=cols, tablefmt=tablefmt)
    if isprint.lower() == 'true':
       print(t)
    return t