openerp.web_quick_print = function (instance) {

    instance.web.ActionManager.include({
        ir_actions_report_xml: function (action, options) {
            action = _.clone(action);

            var eval_contexts = ([instance.session.user_context] || []).concat([action.context]);
            action.context = instance.web.pyeval.eval('contexts', eval_contexts);

            if (!action.report_file) {
                this._super.apply(this, arguments);
                return;
            }

            var doc = _.defaults({
                type: action.report_type,
                title: action.display_name,
                name: action.report_name,
                ids: action.context.active_ids.join(',')
            });

            printJS({
                printable: '/report/' + doc.type.replace(/(qweb-)/g, '') + '/' + doc.name + '/' + doc.ids,
                title: doc.title,
                onLoadingStart: instance.web.blockUI(),
                onLoadingEnd: instance.web.unblockUI()
            });
        }
    });
}