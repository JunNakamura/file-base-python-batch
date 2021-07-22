# file-base-python-batch

This is a reference implement for file base batch to associate external system.

External System A:
1. put input.csv to NFS input directory
2. put end file (empty file) also which means that putting input files is done. 

This Batch:
1. check whether end file exists in NFS input directory
2. start process if and only if end file exists
3. move input file to work directory with gzip compress
4. create gzip compressed result file at work directory
5. copy result file with decompress to NFS output directory (and put end file also)  
6. move files in work directory to backup directory
7. remove work directory

External System B:
1. check whether end file exists in NFS output directory
2. retrieve result.csv if and only if end file exists

## How to use

```commandline
cd batch
python setup.py install # only the first time
python main.py
```

test files are in nfs/test/
