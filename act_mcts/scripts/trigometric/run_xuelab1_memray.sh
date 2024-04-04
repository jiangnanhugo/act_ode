#!/usr/bin/zsh
set -x



basepath=/home/jiang631/data/scibench
py3=/home/jiang631/miniconda3/envs/py310/bin/python3.10
type=$1
nv=$2
nt=$3

thispath=$basepath/mcts_and_vsr_mcts
data_path=$basepath/data/unencrypted/equations_trigometric
opt=L-BFGS-B

noise_type=normal
noise_scale=0.0
metric_name=neg_mse
for prog in {0..9};
do
    eq_name=${type}_nv${nv}_nt${nt}_prog_${prog}.in
    echo "submit $eq_name"
   	dump_dir=$basepath/result/${type}_nv${nv}_nt${nt}/$(date +%F)
    if [ ! -d "$dump_dir" ]
    then
    	echo "create dir: $dump_dir"
    	mkdir -p $dump_dir
	fi
	log_dir=$basepath/log/$(date +%F)
	if [ ! -d "$log_dir" ]
	then
    	echo "create dir: $log_dir"
    	mkdir -p $log_dir
	fi
	echo "$dump_dir/prog_${prog}.metric_${metric_name}.noise_${noise_type}${noise_scale}.opt$opt.cvmcts.out"
	nohup memray $thispath/main.py --equation_name $data_path/$eq_name --optimizer $opt  --cv_mcts\
        		--metric_name 'neg_mse' --noise_type $noise_type --noise_scale $noise_scale > $dump_dir/prog_${prog}.metric_${metric_name}.noise_${noise_type}${noise_scale}.opt$opt.cv_mcts.out &

done


