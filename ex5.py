try:
    begin = int(input('begin->'))
    end = int(input('end->'))

    if end < begin:
        end, begin = begin, end
        
    for item in range(begin, end+1):
            if item % 2 != 0:
               print(item, end = " ")

except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')


            
