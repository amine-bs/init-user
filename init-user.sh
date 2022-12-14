curl -X POST \
	-H "Content-Type: application/json" \
	-d '{"database": null, "prefs": { "allow_tracking": "false", "site_locale": "en", "site_name": "onyxia"}, "token": "metabase", "user": { "email": "toto@toto.toto", "first_name": "user", "last_name": "user", "password": "totototo1", "password_confirm": "totototo1", "site_name": "onyxia"}}' \
	"https://cb.lab.sspcloud.fr/api/setup" 
