def get_string_parts(strs):
    final_parts = strs.split("_")
    list_parts = final_parts[-1].split('.')
    print(list_parts)
    final_parts = final_parts[:-1]
    final_parts.extend(list_parts)
  
    return final_parts
    
input_str = "sales_20231231_1400.csv"

print(get_string_parts(input_str))
print("Try programiz.pro")
