 var survey_options = document.getElementById('survey_options');
            var add_more_fields = document.getElementById('add_more_fields');
            var remove_fields = document.getElementById('remove_fields');

            add_more_fields.onclick = function () {
                var newField = document.createElement('input');
                newField.setAttribute('type', 'text');
                newField.setAttribute('name', 'subs[]');
                newField.setAttribute('placeholder', 'Add Scope');
                survey_options.appendChild(newField);
            }

            remove_fields.onclick = function () {
                var input_tags = survey_options.getElementsByTagName('input');
                if (input_tags.length > 2) {
                    survey_options.removeChild(input_tags[(input_tags.length) - 1]);
                }
            }
