import sys

def select(path,attack_pos,attack_sentence):
    h_num=0
    h_value=[]
    h_text=[]

    p_num=0
    p_value=[]

    a_num=0
    a_value=[]
    with open(path) as f:
        content=f.readlines()
    for line in content:
        if line.startswith('S-'):
            sen=line.split('\t')
            sen=sen[1].strip()
            sen_s=sen.split(' ')
            len_s=len(sen_s)
            continue
        if line.startswith('H-'):               
            h_num+=1
            h=line.split('\t')
            h_value.append(float(h[1]))
            h_text.append(h[2][:-1])
            h_length=len(h_text[0])

        if line.startswith('P-'):                   
            p_num+=1
            line_p=line.split('\t')
            p=line_p[1]
            p=p.split(' ')
            p_b=[]
            for i in p:
                p_b.append(float(i))                 
            p_value.append(p_b)

        if line.startswith('A-'):

            a_num+=1
            if line.endswith('\n'):
                a=line[:-1]
            else:
                a=line[:]

            a=a.split('\t')
            a=a[1]
            a_value.append(a)

        if a_num>=5:
            if len_s<=1:
                with open(attack_pos,'a') as a1:
                    a1.write("[-1]")
                    a1.write('\n')
                with open(attack_sentence,'a') as a2:
                    a2.write(str(sen))
                    a2.write('\n')
                h_num=0
                p_num=0
                a_num=0
                h_value.clear()
                h_text.clear()                      
                p_value.clear()                                 
                a_value.clear()
                continue
            h_max=-1
            tag=0
            max_pos=0
            for value in h_value:
                if value>h_max:
                    h_max=value
                    h_max=tag
                tag+=1
            p_max=p_value[max_pos][:]

            h_text_word=str(h_text[max_pos]).split(' ')
            h_length=len(h_text_word)

            min=0
            pos=-1
            for i in range(h_length):
                if p_value[max_pos][i] < min :
                    pos=i
                    min=p_value[max_pos][i]

            temp_src=0
            temp_trg=0
            arr_src=[]
            arr_tag=[]
            flag=0

            for i in a_value[max_pos]:
                if i=='-'or i==' ':
                    flag+=1
                    continue
                if flag==0:
                    temp_src=temp_src*10+int(i)
                elif flag%2==0:
                    if temp_src==0:
                        arr_tag.append(temp_trg)
                    temp_trg=0
                    temp_src=temp_src*10+int(i)

                if flag%2==1:
                    if temp_trg==0:
                        arr_src.append(temp_src)
                    temp_src=0
                    temp_trg=temp_trg*10+int(i)
                if temp_trg>=h_length-1:
                    break
            arr_tag.append(temp_trg)  

            attack_src_pos=-1
            flag=0
            for i in range(len(arr_tag)):
                if arr_tag[i]==pos:
                    if arr_src[i]>=len_s:
                        flag=1
                    attack_src_pos=arr_src[i]
                    break

            

            with open(attack_pos,'a') as a1:
                if flag==0:
                    pos_list=[]
                    pos_list.append(attack_src_pos)
                    a1.write(str(pos_list))
                    a1.write('\n')
                else:
                    a1.write("[-1]")
                    a1.write('\n')
            with open(attack_sentence,'a') as a2:
             
                a2.write(str(sen))
                a2.write('\n')
            h_num=0
            p_num=0
            a_num=0
            h_value.clear()
            h_text.clear()                      
            p_value.clear()                                 
            a_value.clear()
        


if __name__=='__main__':
    data_file=sys.argv[1]
    attack_pos=sys.argv[2]
    attack_sentence=sys.argv[3]
    select(data_file,attack_pos,attack_sentence)

