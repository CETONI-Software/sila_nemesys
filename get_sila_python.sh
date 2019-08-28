#!/bin/bash
#
# Florian Meinicke
# 2019-08-28
#
# Prepares the sila_python library for installation to work properly
# with the neMESYS SiLA drivers
#
#set -x

# get sila_python
cd ..
git clone https://gitlab.com/SiLA2/sila_python && cd sila_python

# get the new error handling
git merge --no-edit -s recursive -X theirs origin/codegenerator-mod
git merge --no-edit origin/patch-error-handling
git rm sila_library/sila2lib/sila_error_handling.py
git commit --no-edit

# fix files affected by the error handling
sed -i 's/import sila2lib.sila_error_handling as serh/import sila2lib.error_handling.sila_server as serh/' sila_library/sila2lib/std_features/SiLAService.py
sed -i ':a;N;$!ba;s/serh.validationError(.*Identifier")/raise serh.SiLAValidationError(\n                parameter="QualifiedFeatureIdentifier.Identifier",\n                 msg="Feature [{}] not available. Please provide a valid Qualified Feature Identifier".format(feature_id)\n            ).raise_rpc_error(context)/' sila_library/sila2lib/std_features/SiLAService.py
