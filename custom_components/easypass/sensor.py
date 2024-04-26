"""Platform for sensor integration."""
from __future__ import annotations

import logging
from datetime import timedelta
from pprint import pformat

# Import the device class from the component that you want to support
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.components.sensor import (
    PLATFORM_SCHEMA,
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import CONF_NAME, CONF_OFFSET, CONF_PASSWORD, CONF_USERNAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .easypass import EasyPassInstance

_LOGGER = logging.getLogger("easypass")

# Validation of the user's configuration
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_NAME): cv.string,
        vol.Required(CONF_USERNAME): cv.string,
        vol.Required(CONF_PASSWORD): cv.string,
        vol.Required(CONF_OFFSET): cv.string,
    }
)


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the EasyPass Sensor platform."""
    # _LOGGER.info(pformat(config))

    username = config[CONF_USERNAME]
    password = config[CONF_PASSWORD]
    sensor = {
        "name": config[CONF_NAME],
        "offset": config[CONF_OFFSET],
        "username": config[CONF_USERNAME],
        "password": config[CONF_PASSWORD],
    }

    add_entities([EasyPassSensor(sensor)], True)


class EasyPassSensor(SensorEntity):
    """Representation of an EasyPass Sensor."""

    def __init__(self, sensor) -> None:
        """Initialize an EasyPass Login."""
        _LOGGER.info(pformat(sensor))

        self._name = sensor["name"]
        self._value = EasyPassInstance(sensor)
        self._attr_unique_id = sensor["name"]

    @property
    def name(self) -> str:
        """Return the display name of this EasyPass."""
        return self._name

    @property
    def unit_of_measurement(self) -> str:
        """Return the unit of measurement."""
        return "THB"

    def update(self) -> None:
        # _LOGGER.info(self._value.value)
        _state, _attr = self._value.value
        self._attr_native_value = _state
        self.extra_state_attributes = _attr
