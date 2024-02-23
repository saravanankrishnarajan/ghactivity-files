def to_files(df,tgt_dir,file_format):
    print(tgt_dir)
    print(file_format)
    df.coalesce(16). \
        write. \
        partitionBy('year','month','day'). \
        mode('append'). \
        format(file_format). \
        save(tgt_dir)
