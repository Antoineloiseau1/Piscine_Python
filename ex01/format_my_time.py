from datetime import datetime
import time

epoch = time.time()
print("Seconds since January 1, 1970:", f"{epoch:,.4f}", "or", f"{epoch:.2e}", "in scientific notation")
today = datetime.now()
datestr = today.strftime('%b %d %Y')
print(datestr)