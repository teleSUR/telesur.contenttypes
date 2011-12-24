#! /bin/sh

I18NDOMAIN="telesur.contenttypes"

# Synchronise the templates and scripts with the .pot.
# All on one line normally:
bin/i18ndude rebuild-pot --pot src/telesur/contenttypes/locales/${I18NDOMAIN}.pot \
    --create ${I18NDOMAIN} \
    src/telesur/contenttypes

# Synchronise the resulting .pot with all .po files
for po in src/telesur/contenttypes/locales/*/LC_MESSAGES/${I18NDOMAIN}.po; do
    bin/i18ndude sync --pot src/telesur/contenttypes/locales/${I18NDOMAIN}.pot $po
done
