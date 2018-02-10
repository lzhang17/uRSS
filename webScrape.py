import requests
#'Cookie':'aws-target-static-id=1517593221574-77698; aws-target-data=%7B%22support%22%3A%221%22%7D; aws-target-visitor-id=1517593221579-118822.17_38; s_fid=134BAB9B79B38D19-0C4110A32CCF8242; s_vn=1549129222427%26vn%3D1; aws-ubid-main=474-2848758-1406652; aws-session-id=132-3010191-3866316; regStatus=registered; aws-session-id-time=2148475707l; aws-session-token="e7db8B7qB4OW09uYGs6kCZv3H+L4yOFCFLmNbOqtD8zLlswT6IsKGE6q7N46ocg03RiyQ3pD3DKjRZYCVM9hVadMBAzozC5JxBgqQ93uyP2UJpl3RQiwZ4x7BNbFYkbnRGrZuYQ0DSbrJ1YCriY1CSCrpECged9l8jYSEm5xyFwXGBNyEtfLmwEoB05kiPMh6yHq9K+asb2klYLyo7Pea0oVkq6UIfSpxnUTyoK8vYc="; aws-x-main="1dF1K7xpuyGyfsV7BhQnNg9LV5haUygd3y8XMfev?SDxgi?Yp9egXOLf@fQsJoHw"; aws-at-main=Atza|IwEBIHw8uOp88QxwKqKivprOM9XmUmkLivKYw4CnpjR_cBhOiJ7_SYirZA5dOPo6qxc5RlDjGoALwANQZHfmwbU6Qak0uCLaPZY_XCmdaMDHjRDxzXnppIbze8cBxUNfrU2gZ36J9FQrQ35aU-cvxxW4OUh1PgseEneqOexxIBDzUgXs9Beo9thHO8NDiZ_tacKCA4ys8GufzKxHD-FXeq-PP94dNIrNm08BG7_bVskV7fzcm8IdnBGvkbbSCg0l8xijftD3P-I0Mb2sNUxbD8NSoqpS6fD3JQJxgo5laicPGRf0CP0v_0YkVngLy4RbygURvYljlvq_D2gX5wcCGbkFR6UhoI9jX887YlVCG22mgEDG4m4DtJskgrlUGo4k80HPVkwY0fa2wxKLOhPA05fJagLsuwib_D_MgpASOJPrBeriYQ; sess-aws-at-main="qHoStOsYPgJM3Kyrc9StDymTZjtyEjdI07PzooJszN8="; aws-userInfo=%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A753537671611%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22Shane%22%2C%22keybase%22%3A%226vgRVWBmt%2FhQd6%2FMy%2FvB1Xp1Yhi6594urMVvmQ5l5XA%5Cu003d%22%2C%22issuer%22%3A%22https%3A%2F%2Fwww.amazon.com%2Fap%2Fsignin%22%7D; __utmv=194891197.%221dF1K7xpuyGyfsV7BhQnNg9LV5haUygd3y8XMfev%3FSDxgi%3FYp9egXOLf%40fQsJoHw%22; __utma=194891197.332455620.1517593296.1518222893.1518222929.6; __utmc=194891197; __utmz=194891197.1518222929.6.5.utmccn=(referral)|utmcsr=amazon.com|utmcct=/ap/signin|utmcmd=referral; skin=noskin; s_cc=true; s_vnum=1950228475583%26vn%3D1; s_invisit=true; s_dslv_s=More%20than%207%20days; session-id-time=2082787201l; s_sq=%5B%5BB%5D%5D; at-main=Atza|IwEBIGJGGDoha8fuY96uz6eV3FMECWEVf07zhvN6V9nXA2CWqvqARbSS0u8MugRJiwTCHqrJFLp7yl-kPcYHEbRWdxBaxqDOfxbGkJoQ8KSqL1KCiyACd6l6-6DcE5TwiMBsoqJgyv6h90VpkbSoj7Ij6RZ-yxciq603fG1-pbRtVu9TCE3KV8EMv0vV0y01sWDvYwefCM1gWCFIFF8zvd7CSFXRlJ2V2VPORLek46BDPjoi7keO6KcVk18tKPTgsqDeayJsOHIP7nwnZbOefCxcxXYFKYVKZ6BCouu_ZkYZZjSRvNEhe8YuGzmNDVLXxnIpto-eTBsKijW5ncKqDgcseyFfCrDHhF68n07y6-sR0lgL-AlfoCUeVBuQWraEkigO2z1-dIzpnHO8mapuhbNuUVxh; sess-at-main="ag+YRBHb0FVhrjwNpzyjg4tyRcDgIhNAsw+d5H5co78="; sst-main=Sst1|PQEjUN94FGxRq9kPiovyxrYKCC7sx2kO-k2VPN924HJanlYz_w9B4GlTs9SzSxDrtDZW5McePFRa9P_388KATJMmEUhgv2QTYHbYNqaHGbsas2g27xWOMMSvb1MKuszsYj82jHvSoTjZvAJylOjJcD43FO8zL1ZYJdQw6ZOK2RBXKiBvRWEnP-cbHfVh7qMl_PQ64HPNeRjuaMKKIcRaHhH-gYKwQsEQNQ-jmIC-tuEwPYnHJNDKUmtCQXyicI2KpX39DEzqx3B_y7YV-S8VYUe_og; lc-main=en_US; x-wl-uid=1rQJRw+V5NjKUR8EuQpt3yLmGrhniz2ac6aQFBlGzoXwOKfXjlmOu1R2qge7oes4u3DdgjEEnijuvmrdDFNSDLCR4rwHyhuUh5dB/BRd1B3lyUnpRnaweeuypkPPhp4wBARnMTqlGk+8=; s_c27=202074010; s_ppv=57; s_nr=1518229036434-Repeat; s_dslv=1518229036435; session-id=132-9480386-9497655; ubid-main=130-2085283-8402441; session-token="TWCEtKSU8oAUdoroMG4sWoqenkfI2vHULEW7pXw7tqQuDr8//cVGpfrxRTOcE3MndvePT8Hg/YvHPU5QqaWbAyAvruunROulYfm5BrYwSbB8XHvcEvzPQY/V2E8JeS6KjQxbj+N+tzuy4isvrVc2jScmHqnLgNgRj+L9kk4vMJIgUo5EFMDT2yFfkmPnX1zWDhcFk1W2c8qYdh7m0o50es24yuulz37eLP+VEANgIpMETknoJ98CwVal4Lcazy02p3XVQBN0MBYMIyPHYBCWaQ=="; x-main="ivF1uCbEktNbm2m3HiaG?u?jDzrAQNhlsUxTckEuSCIhXiiIYxkiOUx6b7EYfz6E"; csm-hit=MPM220CYR1WPNHZ8QN6E+sa-T3NSCQGJBEYAWFTWX5AZ-S351JVC0MX9QCQCW9W19|1518230431169',
def get_page_content(url=None,headers=None):
  if headers is None: 
    headers = {
      'Accept':'*/*',
      'Accept-Encoding': 'gzip, deflate, br',
      'Accept-Language': 'en-US,en;q=0.9,es;q=0.8',
      'Connection':'keep-alive',
      'DNT':'1',
      'Host':'www.amazon.com',
      'Referer':'https://www.amazon.com/s/ref=sr_st_price-asc-rank?keywords=gaming+gloves&rh=n%3A468642%2Ck%3Agaming+gloves&qid=1518230048&sort=price-asc-rank',
      'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    }
  if url is None: url = 'https://www.amazon.com/s/ref=sr_st_price-asc-rank?keywords=gaming+gloves&rh=n%3A468642%2Ck%3Agaming+gloves&qid=1518230048&sort=price-asc-rank'
  r=requests.get(url,headers=headers)
  tree = html.fromstring(r.content)
  return tree

def parse_page(page):
  #parses the 

html.open_in_browser(tree)