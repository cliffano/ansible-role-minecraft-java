from conflog import Conflog
import minecraftverse
import yaml

cfl = Conflog(conf_files=['./config/conflog.yaml'])
logger = cfl.get_logger('gen-vars-file')

def retrieve_versions_data():
    logger.info('Retrieving versions data...')

    data = {
        'minecraft_versions': {}
    }

    launchermeta_conf = minecraftverse.Configuration(
      host = 'https://launchermeta.mojang.com'
    )
    piston_conf = minecraftverse.Configuration(
      host = 'https://piston-meta.mojang.com'
    )

    with minecraftverse.ApiClient(launchermeta_conf) as launchermeta_api_client:

        launchermeta_api = minecraftverse.DefaultApi(launchermeta_api_client)

        manifest = launchermeta_api.get_minecraft_version_manifest()
        for version in manifest.versions:
            version_url_parts = version.url.split('/')
            package_id = version_url_parts[-2]

            with minecraftverse.ApiClient(piston_conf) as piston_api_client:

                piston_api = minecraftverse.DefaultApi(piston_api_client)

                try:

                    logger.info(f'Retrieving package info for version {version.id} with package ID {package_id} ...')

                    # version.id value is not URL encoded, we offload the encoding to the API client.
                    # For version that has spaces in the name, we must pass the non-URL-encoded value.
                    version_package_info = piston_api.get_minecraft_version_package_info(package_id, version.id)

                    if (version_package_info.downloads.server is None):
                        logger.error(f'No server jar found for version {version.id} with package ID {package_id}')
                        continue

                    data['minecraft_versions'][version.id] = {
                        'url': version_package_info.downloads.server.url,
                        'sha1': version_package_info.downloads.server.sha1
                    }

                except minecraftverse.exceptions.NotFoundException as e:
                    logger.error(f'Unable to find package info for version {version.id} with package ID {package_id}')

    logger.info('Versions data retrieved successfully')
    return data

def write_vars_file(data, file_path):
    logger.info(f'Writing vars file at {file_path} ...')
    vars_data_in_yaml = yaml.dump(data)
    with open(file_path, 'w') as file:
        file.write(vars_data_in_yaml)
        logger.info('Vars file written successfully')

data = retrieve_versions_data()
write_vars_file(data, 'vars/main.yml')