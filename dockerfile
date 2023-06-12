FROM codeits/ms-base-api:0.0.6

ARG GIT_HOST=bitbucket.org
ARG GIT_WORKSPACE=code-business
ARG BRANCH_LIB_CODEITS=master

#remove base tests
RUN rm -rf /api-run/apis
RUN rm -rf /api-run/db
RUN rm -rf /api-run/services
RUN rm -rf /api-run/tests

#copy new files
COPY . /api-run

#RUN bash /api-run/sh/install_libs.sh
VOLUME [ "/api-run/htmlcov" ]
RUN bash /api-run/sh/run_tests.sh

