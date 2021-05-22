import secrets

def genFile(f, size):
  line_len = 64
  for i in range(int(size/line_len)):
    f.write(secrets.token_hex(line_len) + "\n")
  f.close()

genFile(open("small.txt", "w"), 512)
genFile(open("medium.txt", "w"), 2048)
genFile(open("large.txt", "w"), 4096)
