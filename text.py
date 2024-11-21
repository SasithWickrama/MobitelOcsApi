import db
class getNumber:
    def clarityDb(self):
        try:
            conn = db.DbConnection.dbconnClarity(self="")
            with conn.cursor() as c:

                sql = 'SELECT C.CIRT_DISPLAYNAME,C.CIRT_SERT_ABBREVIATION,C.CIRT_STATUS ,SA.SATT_ATTRIBUTE_NAME,SA.SATT_DEFAULTVALUE ' \
                      'FROM CIRCUITS C,SERVICES_ATTRIBUTES SA WHERE CIRT_DISPLAYNAME = :CIRT_DISPLAYNAME AND CIRT_SERV_ID = SATT_SERV_ID ' \
                      'and CIRT_STATUS in (\'INSERVICE\',\'SUSPENDED\') AND SATT_ATTRIBUTE_NAME IN (\'CUSTOMER CONTACT NO\',\'CUSTOMER CONTACT\')'
                c.execute(sql, [self])

                for row in c:
                    result = row[4]

            return result


        except Exception as e:
            result['data']= {"status": "error","errors": "DB Connection Error " + str(e)}
            #logger.info("Exception : %s" % ref + " - " + str(e))
            #logger.info("Exception get number" + str(e) )
            return result

getmobile = getNumber.clarityDb('0113493122')
print(getmobile)
