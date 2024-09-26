print("hello world v2")

""" 
 aws s3 sync . s3://dp-codebase-dev --exclude ".git/*" --exclude ".github/*" --delete

 aws s3 sync . s3://dp-codebase-dev --exclude ".git/*" --exclude ".github/*" --exact-timestamps

  aws s3 sync . s3://dp-codebase-dev/Python-CiCd-Test --exclude ".git/*" --exclude ".github/*" --exact-timestamps --debug

  aws s3 sync . s3://dp-codebase-dev/Python-CiCd-Test --exclude ".git/*" --exclude ".github/*" --size-only

  aws s3 sync . s3://dp-codebase-dev/Python-CiCd-Test --exclude ".git/*" --exclude ".github/*" --exact-timestamps --size-only cd
"""
