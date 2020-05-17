#!/bin/bash

if [ -n $1 ] 
then
	logfile="/mnt/Backup/jails/backup.log"
	jailname=$1

	echo "-------- Starting Backup of FreeNAS Jail $jailname --------" >> $logfile
	echo $(date) >> $logfile

	#Jail #1 Backup
	echo "...Starting jail backup" >> $logfile
	echo $(date) >> $logfile
	echo "...Stopping jail"  >> $logfile
	iocage stop $jailname >> $logfile
	echo "...Exporting jail"  >> $logfile
	iocage export $jailname >> $logfile
	echo "...Starting jail"  >> $logfile
	iocage start $jailname >> $logfile
	echo "...Deleting old backups" >> $logfile
	echo $(date) >> $logfile
	rm /mnt/Backup/jails/$jailname* >> $logfile
	echo "...Moving current backup to stotage folders" >> $logfile
	echo $(date) >> $logfile
	mv -v /mnt/NASData/iocage/images/$jailname* /mnt/Backup/jails/ >> $logfile
	echo "...Done" >> $logfile
	echo $(date) >> $logfile
fi
