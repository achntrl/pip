from pkg_resources import safe_name
import os.path

def substitute(target_relpath):
    filename = os.path.basename(target_relpath)
    name, ext = os.path.splitext(filename)

    wheel_distribution_name, package_version, _, _, _ = name.split('-')
    assert wheel_distribution_name.startswith('datadog_')

    standard_distribution_name = safe_name(wheel_distribution_name)

    # These names are the exceptions.
    if wheel_distribution_name in set([ "datadog_checks_base",
                                        "datadog_checks_dev",
                                        "datadog_checks_tests_helper" ]):
        package_github_dir = wheel_distribution_name
    else:
        package_github_dir = wheel_distribution_name[8:]

    return {
        'wheel_distribution_name': wheel_distribution_name,
        'package_version': package_version,
        'package_github_dir': package_github_dir,
        'standard_distribution_name': standard_distribution_name
    }
