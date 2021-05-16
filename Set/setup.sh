echo "서비스 등록 세팅 실행 \n\n\n"

sudo sudo cp ./Backup-API.service /lib/systemd/system/
systemctl daemon-reload
systemctl enable Backup-API
systemctl restart Backup-API
echo "API 서비스 설정 완료\n"

sleep 15s

service Backup-API status