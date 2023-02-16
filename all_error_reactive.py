@auth.requires_permission('default', 'manager')
def recheck_provioned():
    chunks=1000
    from datetime import datetime, timedelta
    import logging,csv
    now = datetime.now()
    date_time = now.strftime("%Y%m%d")
    import time
    t0 = time.time()
    from gluon import storage
    o = storage.Storage(total=0, found=0, not_found=0, error=0)
    q = db.iccid.fetched == True
    q &= ((db.iccid.error_text==None) | (db.iccid.error_text=='HSS_NULL_MSISDN') | (db.iccid.error_text=='Found in HSS dump'))
    j=0
    for i in db(q).select():
        o.total += 1
        if rdb8.sismember('hss_imsi', i.imsi):
            o.found += 1
            #logger.debug((f'Found ICCID in hss dump, ignoring', i.id, i.name, i.imsi))
        else:
            o.not_found += 1
            j += 1
            #filename = '/tmp/' + 'not_exists_hss_' + date_time + '.csv'
            #with open(filename, 'a') as f:
            #    f.write(f'''{str(i.id)},{str(i.name)},{str(i.imsi)}\n''')
           # logger.info((f'NOT Found ICCID in hss dump, activating', i.id, i.name, i.imsi,j))
            #db(db.iccid.id==i.id).update(active=True, fetched=False, error=False, error_text='Not found in HSS Dump', error_on=request.now, found_in_hss_dump=False, found_in_hlr=False)
            #db(db.provisioned_log.iccid==i.name).update(note='manually removing from provisioned_log')
            if  j > chunks:
             #   db.commit()
                j=0
            #db(db.transaction.iccid==i.id).update(note='removed from provisioned_log')
    return response.json(dict(now=request.now, o=o, time=time.time()-t0))
