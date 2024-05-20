#!/usr/bin/zsh
basepath=/home/$USER/data/act_ode
py3=/home/$USER/miniconda3/envs/py310/bin/python3.10
#
type=Strogatz
method=e2etransformer

noise_type=normal
noise_scale=0.0
metric_name=inv_mse
num_init_conds=5
nvars=$1
total_progs=$2
set -x
for ei in {1..${total_progs}}; do
	eq_name=${nvars}_prog${ei}
	echo "submit $eq_name"

	dump_dir=$basepath/result/${type}/$(date +%F)
	echo $dump_dir
	if [ ! -d "$dump_dir" ]; then
		echo "create output dir: $dump_dir"
		mkdir -p $dump_dir
	fi
	$py3 $basepath/baselines/E2ETransformer/main.py --equation_name $eq_name --pretrained_model_filepath $basepath/baselines/E2ETransformer/model.pt --mode cuda \
		--metric_name $metric_name --num_init_conds $num_init_conds --noise_type $noise_type --noise_scale $noise_scale >$dump_dir/${eq_name}.noise_${noise_type}${noise_scale}.$method.out
done