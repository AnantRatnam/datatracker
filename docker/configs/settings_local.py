# Copyright The IETF Trust 2007-2025, All Rights Reserved
# -*- coding: utf-8 -*-

from ietf.settings import *  # pyflakes:ignore
from ietf.settings import (
    ARTIFACT_STORAGE_NAMES,
    STORAGES,
    BLOBSTORAGE_MAX_ATTEMPTS,
    BLOBSTORAGE_READ_TIMEOUT,
    BLOBSTORAGE_CONNECT_TIMEOUT,
)

ALLOWED_HOSTS = ['*']

from ietf.settings_postgresqldb import DATABASES  # pyflakes:ignore
DATABASE_ROUTERS = ["ietf.blobdb.routers.BlobdbStorageRouter"]
BLOBDB_DATABASE = "blobdb"
BLOBDB_REPLICATION = {
    "ENABLED": True,
    "DEST_STORAGE_PATTERN": "r2-{bucket}",
    "INCLUDE_BUCKETS": ARTIFACT_STORAGE_NAMES,
    "EXCLUDE_BUCKETS": ["staging"],
    "VERBOSE_LOGGING": True,
}

IDSUBMIT_IDNITS_BINARY = "/usr/local/bin/idnits"
IDSUBMIT_STAGING_PATH = "/assets/www6s/staging/"

AGENDA_PATH = '/assets/www6s/proceedings/'
MEETINGHOST_LOGO_PATH = AGENDA_PATH

USING_DEBUG_EMAIL_SERVER=True
EMAIL_HOST='localhost'
EMAIL_PORT=2025

MEDIA_BASE_DIR = '/assets'
MEDIA_ROOT = MEDIA_BASE_DIR + '/media/'
MEDIA_URL = '/media/'

PHOTOS_DIRNAME = 'photo'
PHOTOS_DIR = MEDIA_ROOT + PHOTOS_DIRNAME

SUBMIT_YANG_CATALOG_MODEL_DIR = '/assets/ietf-ftp/yang/catalogmod/'
SUBMIT_YANG_DRAFT_MODEL_DIR = '/assets/ietf-ftp/yang/draftmod/'
SUBMIT_YANG_IANA_MODEL_DIR = '/assets/ietf-ftp/yang/ianamod/'
SUBMIT_YANG_RFC_MODEL_DIR   = '/assets/ietf-ftp/yang/rfcmod/'

# Set INTERNAL_IPS for use within Docker. See https://knasmueller.net/fix-djangos-debug-toolbar-not-showing-inside-docker
import socket
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips] + ['127.0.0.1']

# DEV_TEMPLATE_CONTEXT_PROCESSORS = [
#    'ietf.context_processors.sql_debug',
# ]

DOCUMENT_PATH_PATTERN = '/assets/ietfdata/doc/{doc.type_id}/'
INTERNET_DRAFT_PATH = '/assets/ietf-ftp/internet-drafts/'
RFC_PATH = '/assets/ietf-ftp/rfc/'
CHARTER_PATH = '/assets/ietf-ftp/charter/'
BOFREQ_PATH = '/assets/ietf-ftp/bofreq/'
CONFLICT_REVIEW_PATH = '/assets/ietf-ftp/conflict-reviews/'
STATUS_CHANGE_PATH = '/assets/ietf-ftp/status-changes/'
INTERNET_DRAFT_ARCHIVE_DIR = '/assets/collection/draft-archive'
INTERNET_ALL_DRAFTS_ARCHIVE_DIR = '/assets/archive/id'
BIBXML_BASE_PATH = '/assets/ietfdata/derived/bibxml'
IDSUBMIT_REPOSITORY_PATH = INTERNET_DRAFT_PATH
FTP_DIR = '/assets/ftp'
NFS_METRICS_TMP_DIR = '/assets/tmp'

NOMCOM_PUBLIC_KEYS_DIR = 'data/nomcom_keys/public_keys/'
SLIDE_STAGING_PATH = '/assets/www6s/staging/'

DE_GFM_BINARY = '/usr/local/bin/de-gfm'

STATIC_IETF_ORG = "/_static"
STATIC_IETF_ORG_INTERNAL = "http://static"


# Blob replication storage for dev
import botocore.config
for storagename in ARTIFACT_STORAGE_NAMES:
    replica_storagename = f"r2-{storagename}"
    STORAGES[replica_storagename] = {
        "BACKEND": "ietf.doc.storage.MetadataS3Storage",
        "OPTIONS": dict(
            endpoint_url="http://blobstore:9000",
            access_key="minio_root",
            secret_key="minio_pass",
            security_token=None,
            client_config=botocore.config.Config(
                signature_version="s3v4",
                connect_timeout=BLOBSTORAGE_CONNECT_TIMEOUT,
                read_timeout=BLOBSTORAGE_READ_TIMEOUT,
                retries={"total_max_attempts": BLOBSTORAGE_MAX_ATTEMPTS},
            ),
            verify=False,
            bucket_name=f"{storagename}",
        ),
    }
