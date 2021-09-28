odoo.define("sh_snippet_adv.init_wow_frontend", function (require) {
    "use strict";

    var publicWidget = require("web.public.widget");

    $(document).ready(function () {
        new WOW().init();
    });
});
