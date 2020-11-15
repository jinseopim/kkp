from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import FinanceDataReader as fdr
from django.http import JsonResponse
import json
import pandas as pd


# https://financedata.github.io/posts/finance-data-reader-users-guide.html
# https://github.com/FinanceData/FinanceDataReader
# @login_required
def get_finance_data(request):
    start_date = '2020-11-01'
    end_date = '2020-11-05'

    """
    stock_list = [
        ["AAPL", "AAPL"],
        ["AMZN", "AMZN"],
        ["DJI", "DJI"],
        ["USDKRW", "USD/KRW"],
        # ["삼성전자", "005930"],
        # ["SK하이닉스", "000660"],
        # ["현대차", "005380"],
        # ["셀트리온", "068270"],
        # ["LG화학", "051910"],
        # ["POSCO", "005490"],
        # ["삼성물산", "028260"],
        # ["NAVER", "035420"],
    ]

    df_list = [fdr.DataReader(code, start_date, end_date)['Close'] for name, code in stock_list]
    print(len(df_list))

    df = pd.concat(df_list, axis=1)
    df.columns = [name for name, code in stock_list]

    print(df.head(10))
    """

    appl_df = fdr.DataReader('AAPL', start_date, end_date)['Close']
    amzn_df = fdr.DataReader('AMZN', start_date, end_date)['Close']
    dji_df = fdr.DataReader('DJI', start_date, end_date)['Close']
    usd_krw_df = fdr.DataReader('USD/KRW', start_date, end_date)['Close']

    context = {
        "appl_df": appl_df,
        "amzn_df": amzn_df,
        "dji_df": dji_df,
        "usd_krw_df": usd_krw_df,
    }

    print(context)

    return JsonResponse(json.loads(context), safe=False)