import sys
import subprocess


row3s = []


#result = b'{"id":22395,"data":"A\r\n1 2 3 6 7 5 4 \r\n6 4 2 7 5 3 1 \r\n7 5 6 2 1 4 3 \r\n2 1 7 4 3 6 5 \r\n4 7 5 3 2 1 6 \r\n5 3 4 1 6 2 7 \r\n3 6 1 5 4 7 2 \r\nT\r\n  2   0   2   0  35   1   0\r\n  6   2   0  10   0   3   0\r\n 14   4   1   0   0  72   2\r\n  0   0   0   1   0   0   0\r\n 60  35   0   0   3   1  13\r\n  0  18   3   0   0  11   0\r\n  0   0   0   9   0   0   0\r\nS\r\n/ 0 / 0 * - 0\r\n1 - 0 + 0 / 0\r\n* - - 0 0 * -\r\n0 0 0 - 0 0 0\r\n* * 0 0 / 1 +\r\n0 * - 0 0 + 0\r\n0 0 0 + 0 0 0\r\nV\r\n0 1 0 1 1 0\r\n1 0 1 1 1 0\r\n1 1 1 0 1 1\r\n1 1 1 1 0 1\r\n1 0 1 1 1 1\r\n1 1 0 1 1 1\r\n1 0 1 0 1 0\r\nH\r\n1 1 0 1 0 0\r\n1 1 0 1 1 0\r\n1 1 0 1 1 1\r\n1 0 1 0 1 1\r\n0 1 1 1 0 1\r\n1 1 0 1 1 0\r\n1 1 0 1 0 1\r\n\r\n","size":7,"level":"medium","operations":"adms","no":22395,"guest":false,"daily":false,"state":null,"u_level":"B"}'
#result = result.decode("ASCII")

def get_json():
  puzzle = sys.argv[1]
  p = subprocess.run(["./fetch.sh {}".format(puzzle)], shell=True, capture_output=True)
  result = p.stdout
  result = result.decode("ASCII")
  return result

def parse_result(json):
  A_location = json.index('A')
  T_location = json.index('T')
  S_location = json.index('S')
  V_location = json.index('V')
  H_location = json.index('H')
  Size_location = json.index("size")

  A_string = json[A_location:T_location].replace("A",'')
  T_string = json[T_location:S_location].replace("T",'')
  S_string = json[S_location:V_location].replace("S",'')
  V_string = json[V_location:H_location].replace("V",'')
  H_string = json[H_location:Size_location - 3].replace("H",'')




  
  #For some reason the linux server and windows treat these two translations differently. Uncomment this section when testing in linux
  A_list = A_string.split("\\r\\n")
  T_list = T_string.split("\\r\\n")
  S_list = S_string.split("\\r\\n")
  V_list = V_string.split("\\r\\n")
  H_list = H_string.split("\\r\\n")
  
  """ 
  A_list = A_string.split("\r\n")
  T_list = T_string.split("\r\n")
  S_list = S_string.split("\r\n")
  V_list = V_string.split("\r\n")
  H_list = H_string.split("\r\n")
  """
  
  A = [i.split(' ') for i in A_list if not i == '']
  T = [i.split('  ') for i in T_list if not i == '']
  S = [i.split(' ') for i in S_list if not i == '']
  V = [i.split(' ') for i in V_list if not i == '']
  H = [i.split(' ') for i in H_list if not i == '']

  for row in A:
    if '' in row:
      row.remove('')

  for row in T:
    if '' in row:
      row.remove('')
  
  for i in range(len(T)):
    for j in range(len(T[i])):
      T[i][j] = T[i][j].lstrip(" ")
  

  print(A)
  print(T)
  print(S)
  print(V)
  print(H)

  create_output(A,T,S,V,H)




def create_output(values,result,symbol,wall,floor):
  limit = len(values)
  print("\033[92m"+ "+=========================================+"+ "\033[0m")
  for i in range (limit):
    row1 = "\033[92m" + "|" + "\033[0m"
    row2 = "\033[92m" + "|" + "\033[0m"
    row3 = ""
    for element in range(7):
      total = result[i][element]
      op = symbol[i][element]
      val = values[i][element]
      
      if total == '0':
        row1 += " "
      elif len(total) == 2:
        row1 += total
      else:
        row1 += total

      if op == '0' or op =='1':
        if len(total) == 2:
          row1 += "   "
        else:
          row1 += "    "
      else:
        if len(total) == 2:
          row1 += op + '  '
        else:
          row1+= op + '   '

      row2 += "    " + val


      if element > 5:
        row1 += "\033[92m" + "|" + "\033[0m"
        row2 += "\033[92m" + "|" + "\033[0m"
      else:
        if wall[i][element] == '1':
          row1 +=  "\033[92m" + "|" + "\033[0m"
          row2 +=  "\033[92m" + "|" + "\033[0m"
        else:
          row1 += "|"
          row2 += '|'

      if element > 5:
        row3 = "\033[92m"+ "+=========================================+"+ "\033[0m"
      else:
        row3 = get_row3(floor,element)
      
      row3s.append(row3)
      

    print(row1)
    print(row2)
    print(row3s[i])
    




def get_row3(floor,index):
  row3 =  "+" 
  for i in range(7):
    if floor[i][index] == "1":
      row3 += "\033[92m" + "=====" + "\033[0m" + "+"
    else:
      row3 += "-----" + "+"
  return row3



def main():
  json = get_json()
  #json = result
  parse_result(json)

main()