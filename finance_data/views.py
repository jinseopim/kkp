from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import FinanceDataReader as fdr
from django.http import JsonResponse
import json
import pandas as pd


# https://financedata.github.io/posts/finance-data-reader-users-guide.html
# https://github.com/FinanceData/FinanceDataReader
@login_required
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

    """
    appl_df = fdr.DataReader('AAPL', start_date, end_date)['Close']
    amzn_df = fdr.DataReader('AMZN', start_date, end_date)['Close']
    dji_df = fdr.DataReader('DJI', start_date, end_date)['Close']
    usd_krw_df = fdr.DataReader('USD/KRW', start_date, end_date)['Close']
    """

    appl_df = pd.DataFrame(
        {
            'date': [
                '2020-11-02',
                '2020-11-03',
                '2020-11-04',
                '2020-11-05'
            ],
            'stock': [
                '108.77', '110.44', '114.95', '119.03'
            ]
        }
    )

    amzn_df = pd.DataFrame(
        {
            'date': [
                '2020-11-02',
                '2020-11-03',
                '2020-11-04',
                '2020-11-05'
            ],
            'stock': [
                '3004.48', '3048.41', '3241.16', '3322.00'
            ]
        }
    )

    dji_df = pd.DataFrame(
        {
            'date': [
                '2020-11-02',
                '2020-11-03',
                '2020-11-04',
                '2020-11-05'
            ],
            'stock': [
                '26925.05', '27480.03', '27847.66', '28390.18'
            ]
        }
    )

    usd_krw_df = pd.DataFrame(
        {
            'date': [
                '2020-11-02',
                '2020-11-03',
                '2020-11-04',
                '2020-11-05'
            ],
            'stock': [
                '1132.95', '1131.32', '1127.65', '1122.88'
            ]
        }
    )

    appl_json = appl_df.reset_index().to_json(orient='records')
    amzn_json = amzn_df.reset_index().to_json(orient='records')
    dji_json = dji_df.reset_index().to_json(orient='records')
    usd_krw_json = usd_krw_df.reset_index().to_json(orient='records')

    # appl_res, amzn_res, dji_res, usd_krw_res = []

    appl_res = json.loads(appl_json)
    amzn_res = json.loads(amzn_json)
    dji_res = json.loads(dji_json)
    usd_krw_res = json.loads(usd_krw_json)

    context = {
        'appl_res': appl_res,
        'amzn_res': amzn_res,
        'dji_res': dji_res,
        'usd_krw_res': usd_krw_res,
        "result": "success"
    }

    # print(context, "asdfasdfasdfasdf", type(context))

    return JsonResponse(context, safe=False)