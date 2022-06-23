# Copyright (c) 2021, VRAI Labs and/or its affiliates. All rights reserved.
#
# This software is licensed under the Apache License, Version 2.0 (the
# "License") as published by the Apache Software Foundation.
#
# You may not use this file except in compliance with the License. You may
# obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from typing import TypeVar

from supertokens_python.ingredients.smsdelivery.types import SMSDeliveryTwilioConfig

_T = TypeVar('_T')


def normalize_twilio_config(sms_input: SMSDeliveryTwilioConfig[_T]) -> SMSDeliveryTwilioConfig[_T]:
    from_ = sms_input.twilio_settings.from_
    messaging_service_sid = sms_input.twilio_settings.messaging_service_sid

    if (from_ and messaging_service_sid) or (not from_ and not messaging_service_sid):
        raise Exception('Please pass exactly one of "from" and "messaging_service_sid" config for twilio_settings.')

    return sms_input
