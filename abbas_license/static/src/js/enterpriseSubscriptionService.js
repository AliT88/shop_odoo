/** @odoo-module **/

import {patch} from "@web/core/utils/patch";
import {
    enterpriseSubscriptionService,
    SubscriptionManager
} from "@web_enterprise/webclient/home_menu/enterprise_subscription_service";

patch(enterpriseSubscriptionService, {
    name: "enterprise_subscription",
    dependencies: ["orm", "rpc", "notification"],
    start(env, { rpc, orm, notification }) {
        // registry
        //     .category("main_components")
        //     .add("expired_subscription_block_ui", { Component: ExpiredSubscriptionBlockUI });
        return new SubscriptionManager(env, { rpc, orm, notification });
    },
});

