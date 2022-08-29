import json

import imagehash

import json_dict

if __name__ == '__main__':
    file_list = json_dict.read_info()
    repete_list = []
    for i in range(len(file_list)):
        for j in range(i, len(file_list)):
            hash_i = imagehash.hex_to_hash(file_list[i]['dhash'])
            hash_j = imagehash.hex_to_hash(file_list[j]['dhash'])
            diff = hash_i - hash_j
            if diff <= 5 and diff != 0:
                repete_list.append((file_list[i], file_list[j]))
    if len(repete_list) == 0:
        print("No repet was found")
    else:
        with open('repete_list.json','w') as f:
            f.write(json.dumps(repete_list))
            f.close()
        print(f"{len(repete_list)} was found")
