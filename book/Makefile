# ...
export PROJECT = cvisor
export REQUIREMENTS = dev

# target:
# target: all - Default target. Does nothing
.PHONY: all
all:
	@echo "Hello $(LOGNAME), nothing to do by default"


# target: help - Display callable targets
.PHONY: help
help:
	@egrep "^# target:|-\ .+" [Mm]akefile --color=auto|column -t -s -


# target:
# target: ========= pull ==============

# target: pull_python - pull python images
pull_python:
	@echo "---> pull python:3.6-slim"
	@docker pull python:3.6-slim

# target: pull_all - pull all images in project
pull_all:
	@make pull_python

# target:
# target: ===== build ======= - ============================

# target: build_main - build  image
.PHONY: build_main
build_main:
	@docker-compose \
		-p $(PROJECT) \
		-f build.yml \
		build \
		main


# target:
# target: ===== bootstrap === - ============================


# target: bootstrap - bootstrap  contaner
.PHONY: bootstrap
bootstrap:
	@docker-compose \
		-p $(PROJECT) \
		-f bootstrap.yml \
		run \
		--rm \
		main


# target:
# target: ===== shell ======= - ============================

# target: shell - go in shell container
.PHONY: shell
shell:
	@docker-compose \
		-p $(PROJECT) \
		-f run.yml \
		run \
		--rm \
		--name $(PROJECT)_main_1 \
		main


# target:
# target: ===== misc ======== - ============================

# target: down - run all contaner in project
.PHONY: up
up:
	@docker-compose \
		-p $(PROJECT) \
		-f run.yml \
		up

# target: down - shutdown all contaner in project
.PHONY: down
down:
	@docker-compose \
		-p $(PROJECT) \
		-f run.yml \
		down	


# target: ps - watch all process all contaner in project
.PHONY: ps
ps:
	@docker-compose \
		-p $(PROJECT) \
		-f run.yml \
		ps

# target: clear - clear untuged images in project
.PHONY: clear
clear:
	@../../scripts/clear_untagged.sh


# target: images - show all images in project
.PHONY: images
images:
	@docker images |grep $(PROJECT)


# target: volumes - show all volumes in project
.PHONY: volumes
volumes:
	@docker volume ls |grep $(PROJECT)


# target: rmi - remove all images in project
.PHONY: rmi
rmi:
	@docker rmi `docker images |grep $(PROJECT) |xargs -L1 | awk '{print $1}'`


# target: rmvol - remove all volumes in project
.PHONY: rmvol
rmvol:
	@docker volume rm `docker volume ls |grep $(PROJECT) |xargs -L1 | awk "{print $2}"`
# ...




