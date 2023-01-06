import sys
import csv
import json
import urllib3

def main(_action, _file):
    _test_file = 'datafile/' + _file
    with open(_test_file, "r", encoding="utf-8-sig") as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            user_account = row['user_account']
            user_password = row['user_password']
    
            if _action == "create_user_account":
                url = "Spring-729943055.us-east-1.elb.amazonaws.com/user"
                header = {
                'Content-Type': 'application/json;charset=utf-8'
                }
                body = {
                    "user_account":user_account,
                    "user_password":user_password
                }
                
                http = urllib3.PoolManager()
                res = http.request('POST', url, headers=header, body=json.dumps(body).encode('utf-8'))
                decode_res_str = res.data.decode("UTF-8")
                
                try:
                    print('response body: ' + str(decode_res_str))
                except Exception as e:
                    print(str(decode_res_str))
                    print("Error: " + str(e))
            
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])