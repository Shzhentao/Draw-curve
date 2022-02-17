prefixPath="/mnt/Zhentaob/mycode/AVAC_4/checkpoints/"
suffixPath="/Kinetics/Cross-N65536/eval-ucf101-wucls-8at16/fold-01/"
originfilename="AVAC"
filenames=("AVAC_adco" "AVAC_avc" "AVAC_avid" "AVAC_not_simple_new" "AVAC_simple_new")
cmds=("python eval-action-recg.py configs/benchmark/ucf/8at16-fold1.yaml configs/main/avac/kinetics/Cross-N65536.yaml --distributed --port 12345 --quiet --resume --adco"
      "python eval-action-recg.py configs/benchmark/ucf/8at16-fold1.yaml configs/main/avac/kinetics/Cross-N65536.yaml --distributed --port 12345 --quiet --avc --resume"
      "python eval-action-recg.py configs/benchmark/ucf/8at16-fold1.yaml configs/main/avac/kinetics/Cross-N65536.yaml --distributed --port 12345 --quiet --avc --resume"
      "python eval-action-recg.py configs/benchmark/ucf/8at16-fold1.yaml configs/main/avac/kinetics/Cross-N65536.yaml --distributed --port 12345 --quiet --resume"
      "python eval-action-recg.py configs/benchmark/ucf/8at16-fold1.yaml configs/main/avac/kinetics/Cross-N65536.yaml --distributed --port 12345 --quiet --resume")
checkpoint1="checkpoint.pth.tar"
eval0="eval0.log"
prefixEval="eval"
suffixEval=".log"
config0="config0.yaml"
prefixcheckpoint2="checkpoint-ep"
suffixcheckpoint2=".pth.tar"

for ((num=35; num<=45; num ++))
do
    for((i=0;i<${#filenames[@]};i++)) 
    do
        # 更新配置中训练总批次
        python changeConfig.py --num $num
        # 确定使用的检查点（超前一个）
        exp='expr '$num' - 1'
        num2=`$exp`
        checkpoint2=$prefixcheckpoint2$num2$suffixcheckpoint2
        # 将AVAC*文件夹转换为AVAC文件夹
        mv $prefixPath${filenames[i]} $prefixPath$originfilename
        # 得到工作文件夹
        wholePath=$prefixPath$originfilename$suffixPath
        # 删除checkpoint.pth.tar检查点
        rm $wholePath$checkpoint1
        # 复制选定的检查点到checkpoint.pth.tar检查点
        cp $wholePath$checkpoint2 $wholePath$checkpoint1
        # 运行下游任务命令
        ${cmds[i]}
        # 将生成的eval0.log文件重命名为相应批次
        cp $wholePath$eval0 $wholePath$prefixEval$num$suffixEval
        # 删除eval0.log文件和config0.yaml文件
        rm $wholePath$config0 $wholePath$eval0
        # 将AVAC文件夹转换为AVAC*文件夹
        mv $prefixPath$originfilename $prefixPath${filenames[i]}
    done
done