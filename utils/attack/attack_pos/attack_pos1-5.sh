m2_file=$1

# cd CSA-Grammatical-Error-Correction/utils/attack/attack_pos
pos_dir='poslist'
mkdir -p $pos_dir

pos1=$pos_dir/attack_pos_1
pos2=$pos_dir/attack_pos_2
pos3=$pos_dir/attack_pos_3
pos4=$pos_dir/attack_pos_4
pos5=$pos_dir/attack_pos_5
sen=$pos_dir/attack_sen

python attack_pos_get_1.py $m2_file $pos1 $sen
python attack_pos_get_2-5.py $m2_file $pos2 2
python attack_pos_get_2-5.py $m2_file $pos3 3
python attack_pos_get_2-5.py $m2_file $pos4 4
python attack_pos_get_2-5.py $m2_file $pos5 5