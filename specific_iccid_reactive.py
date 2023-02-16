def reactive_iccid():
    iccid_list=['8993017100276530588F', '8993017100276530695F','8993017100276547434F', '8993017100276445241F', '8993017100276445316F', '8993017100276458434F',  '8993017100276387286F', '8993017100276400865F','8993017100276285134F', '8993017100276294151F','8993017100276298145F', '8993017100276301535F', '8993017100276437099F',  '8993017100276439178F', '8993017100276444905F', '8993017100276528285F',  '8993017100276528343F', '8993017100276591143F', '8993017100276592539F', '8993017100276603898F','8993017100276611321F', '8993017100276618813F', '8993017100276622955F', '8993017100276608228F', '8993017100276411110F', '8993017100276411169F']
    for iccid in iccid_list:
        for row in db((db.iccid.name==iccid)).select():
            logger.info(("reactivating_iccid ", row.name, row.imsi, row ))
def reactive_iccid():
    success = 0
    found = 0
    total = 0 
    error = 0
    iccid_list=['8993017100276530588F', '8993017100276530695F','8993017100276547434F', '8993017100276445241F', '8993017100276445316F', '8993017100276458434F',  '8993017100276387286F', '8993017100276400865F','8993017100276285134F', '8993017100276294151F','8993017100276298145F', '8993017100276301535F', '8993017100276437099F',  '8993017100276439178F', '8993017100276444905F', '8993017100276528285F',  '8993017100276528343F', '8993017100276591143F', '8993017100276592539F', '8993017100276603898F','8993017100276611321F', '8993017100276618813F', '8993017100276622955F', '8993017100276608228F', '8993017100276411110F', '8993017100276411169F']
    for iccid in iccid_list:
        for row in db((db.iccid.name==iccid)).select():
            try:
                sql = ch.execute(f"select msisdn, imsi from hss where imsi='{row.imsi}' ")
                if not sql:
                    logger.info(("reactivating_iccid ", row.name, row.imsi, row ))
                    #db(db.iccid.id==row.id).update(active=True, error=False, error_text='reactive by fariba', reserved=False, found_in_hss_dump=False, found_in_hlr=False)
                    e = 'error removed Due to not found in HSS DUMP'
                    logger.debug((e, iccid.name, iccid.imsi))
                    success += 1
                else:
                    e = 'found in HSS DUMP'
                    logger.debug((e, row.name, row.imsi, sql ))
                    found += 1
            except Exception as e:
                logger.exception(e)
                error += 1
            
    return dict(list_iccid=len(iccid_list), error=error , total=total , success=success, found= found)
