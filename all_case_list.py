# coding=utf-8
# import sys
# sys.path.append("test_case")
from case_method import login_case,B2bOrders_case

def caseList():
    all_test_case_names=[
        login_case.LoginTest,
        B2bOrders_case.B2bOrdersTest,
    ]

    print "seccess read case list："
    l=len(all_test_case_names)
    for i in range(l):
        print all_test_case_names[i]
    print "count:%d"%l
    return all_test_case_names