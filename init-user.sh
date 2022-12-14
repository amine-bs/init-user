until printf "." && nc -z -w 2 localhost 3000; do
    sleep 2;
done;
echo 'Metabase OK ✓' 

curl -X POST \
	-H "Content-Type: application/json"  \
	-d '{"database": null, "prefs": { "allow_tracking": "false", "site_locale": "en", "site_name": "onyxia"}, "token": "'$MB_SETUP_TOKEN'", "user": { "email": "'$MB_ADMIN_EMAIL'", "first_name": null, "last_name": null, "password": "'$MB_ADMIN_PASSWORD'", "password_confirm": "'$MB_ADMIN_PASSWORD'", "site_name": "onyxia"}}' \
	"localhost:3000/api/setup" &&\
	
echo "Initialization done!" 
echo "sleeping..."
while true; do
    sleep 2
done
