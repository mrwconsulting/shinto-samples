#!/bin/sh
set -e
set +x
set -o pipefail
if [ "${DEBUG}" == "true" ]; then
    set -x
fi

declare -a LIST=("cdk-java" "cdk-python" "cdk-typescript" "jib-gradle" "jib-maven" "python-pip" "python-poetry" "springboot-gradle" "springboot-kotlin" "springboot-maven")

DEFAULT_DIR=$(PWD)/..
DEFAULT_SLEEPTIME=15
read -e -p  "Parent directory: [$DEFAULT_DIR] " PARENT_DIR
PARENT_DIR="${PARENT_DIR:-$DEFAULT_DIR}"
read -e -p  "Sleep time between samples: [$DEFAULT_SLEEPTIME] " SLEEPTIME
SLEEPTIME="${SLEEPTIME:-$DEFAULT_SLEEPTIME}"
for INDEX in "${LIST[@]}"; do
    echo "registering ${INDEX} sample....."
    shinto-manager register $PARENT_DIR/$INDEX/.shinto/props.json
    echo "pausing between registering...${SLEEPTIME} seconds"
    sleep ${SLEEPTIME}
done