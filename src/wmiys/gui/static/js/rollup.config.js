/************************************************************************** 

This is the Rollup.JS configuration file.

***************************************************************************/


class RollupConfig
{
    constructor(input, output) {
        this.input = input;

        this.output = {
            format: 'iife',
            compact: true,
            sourcemap: true,
            file: output,
        }
    }
}


const configs = [
    new RollupConfig('custom/pages/create-account.js', 'dist/create-account.bundle.js'),
    new RollupConfig('custom/pages/home.js', 'dist/home.bundle.js'),
    new RollupConfig('custom/pages/login.js', 'dist/login.bundle.js'),
    new RollupConfig('custom/pages/account-settings/general.js', 'dist/account-settings-general.bundle.js'),
    new RollupConfig('custom/pages/account-settings/requests-submitted/main.js', 'dist/account-settings-requests-submitted.bundle.js'),
    new RollupConfig('custom/pages/password-reset/index.js', 'dist/password-reset-index.bundle.js'),
    new RollupConfig('custom/pages/product-listings/product-listing.js', 'dist/product-listings-product-listing.bundle.js'),
    new RollupConfig('custom/pages/products/inventory.js', 'dist/products-inventory.bundle.js'),
    new RollupConfig('custom/pages/products/overview.js', 'dist/products-overview.bundle.js'),
    new RollupConfig('custom/pages/products/requests/main.js', 'dist/products-requests.bundle.js'),
    new RollupConfig('custom/pages/products/product/availability.js', 'dist/products-product-availability.bundle.js'),
    new RollupConfig('custom/pages/products/product/insights.js', 'dist/products-product-insights.bundle.js'),
    new RollupConfig('custom/pages/products/product/overview/main.js', 'dist/products-product-overview.bundle.js'),
    new RollupConfig('custom/pages/products/product/settings.js', 'dist/products-product-settings.bundle.js'),
    new RollupConfig('custom/pages/search-products/results.js', 'dist/search-products-results.bundle.js'),
];



// rollup.config.js
export default configs;