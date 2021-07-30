# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 11
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class NodeHardwareNode(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'chassis': 'str',
        'chassis_code': 'str',
        'chassis_count': 'str',
        '_class': 'str',
        'configuration_id': 'str',
        'cpu': 'str',
        'disk_controller': 'str',
        'disk_expander': 'str',
        'family_code': 'str',
        'flash_drive': 'str',
        'generation_code': 'str',
        'hwgen': 'str',
        'id': 'int',
        'imb_version': 'str',
        'infiniband': 'str',
        'lcd_version': 'str',
        'lnn': 'int',
        'motherboard': 'str',
        'net_interfaces': 'str',
        'nvram': 'str',
        'powersupplies': 'list[str]',
        'processor': 'str',
        'product': 'str',
        'ram': 'int',
        'serial_number': 'str',
        'series': 'str',
        'storage_class': 'str',
        'tier': 'int'
    }

    attribute_map = {
        'chassis': 'chassis',
        'chassis_code': 'chassis_code',
        'chassis_count': 'chassis_count',
        '_class': 'class',
        'configuration_id': 'configuration_id',
        'cpu': 'cpu',
        'disk_controller': 'disk_controller',
        'disk_expander': 'disk_expander',
        'family_code': 'family_code',
        'flash_drive': 'flash_drive',
        'generation_code': 'generation_code',
        'hwgen': 'hwgen',
        'id': 'id',
        'imb_version': 'imb_version',
        'infiniband': 'infiniband',
        'lcd_version': 'lcd_version',
        'lnn': 'lnn',
        'motherboard': 'motherboard',
        'net_interfaces': 'net_interfaces',
        'nvram': 'nvram',
        'powersupplies': 'powersupplies',
        'processor': 'processor',
        'product': 'product',
        'ram': 'ram',
        'serial_number': 'serial_number',
        'series': 'series',
        'storage_class': 'storage_class',
        'tier': 'tier'
    }

    def __init__(self, chassis=None, chassis_code=None, chassis_count=None, _class=None, configuration_id=None, cpu=None, disk_controller=None, disk_expander=None, family_code=None, flash_drive=None, generation_code=None, hwgen=None, id=None, imb_version=None, infiniband=None, lcd_version=None, lnn=None, motherboard=None, net_interfaces=None, nvram=None, powersupplies=None, processor=None, product=None, ram=None, serial_number=None, series=None, storage_class=None, tier=None):  # noqa: E501
        """NodeHardwareNode - a model defined in Swagger"""  # noqa: E501

        self._chassis = None
        self._chassis_code = None
        self._chassis_count = None
        self.__class = None
        self._configuration_id = None
        self._cpu = None
        self._disk_controller = None
        self._disk_expander = None
        self._family_code = None
        self._flash_drive = None
        self._generation_code = None
        self._hwgen = None
        self._id = None
        self._imb_version = None
        self._infiniband = None
        self._lcd_version = None
        self._lnn = None
        self._motherboard = None
        self._net_interfaces = None
        self._nvram = None
        self._powersupplies = None
        self._processor = None
        self._product = None
        self._ram = None
        self._serial_number = None
        self._series = None
        self._storage_class = None
        self._tier = None
        self.discriminator = None

        if chassis is not None:
            self.chassis = chassis
        if chassis_code is not None:
            self.chassis_code = chassis_code
        if chassis_count is not None:
            self.chassis_count = chassis_count
        if _class is not None:
            self._class = _class
        if configuration_id is not None:
            self.configuration_id = configuration_id
        if cpu is not None:
            self.cpu = cpu
        if disk_controller is not None:
            self.disk_controller = disk_controller
        if disk_expander is not None:
            self.disk_expander = disk_expander
        if family_code is not None:
            self.family_code = family_code
        if flash_drive is not None:
            self.flash_drive = flash_drive
        if generation_code is not None:
            self.generation_code = generation_code
        if hwgen is not None:
            self.hwgen = hwgen
        if id is not None:
            self.id = id
        if imb_version is not None:
            self.imb_version = imb_version
        if infiniband is not None:
            self.infiniband = infiniband
        if lcd_version is not None:
            self.lcd_version = lcd_version
        if lnn is not None:
            self.lnn = lnn
        if motherboard is not None:
            self.motherboard = motherboard
        if net_interfaces is not None:
            self.net_interfaces = net_interfaces
        if nvram is not None:
            self.nvram = nvram
        if powersupplies is not None:
            self.powersupplies = powersupplies
        if processor is not None:
            self.processor = processor
        if product is not None:
            self.product = product
        if ram is not None:
            self.ram = ram
        if serial_number is not None:
            self.serial_number = serial_number
        if series is not None:
            self.series = series
        if storage_class is not None:
            self.storage_class = storage_class
        if tier is not None:
            self.tier = tier

    @property
    def chassis(self):
        """Gets the chassis of this NodeHardwareNode.  # noqa: E501

        Name of this node's chassis.  # noqa: E501

        :return: The chassis of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self._chassis

    @chassis.setter
    def chassis(self, chassis):
        """Sets the chassis of this NodeHardwareNode.

        Name of this node's chassis.  # noqa: E501

        :param chassis: The chassis of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if chassis is not None and len(chassis) > 255:
            raise ValueError("Invalid value for `chassis`, length must be less than or equal to `255`")  # noqa: E501
        if chassis is not None and len(chassis) < 0:
            raise ValueError("Invalid value for `chassis`, length must be greater than or equal to `0`")  # noqa: E501

        self._chassis = chassis

    @property
    def chassis_code(self):
        """Gets the chassis_code of this NodeHardwareNode.  # noqa: E501

        Chassis code of this node (1U, 2U, etc.).  # noqa: E501

        :return: The chassis_code of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self._chassis_code

    @chassis_code.setter
    def chassis_code(self, chassis_code):
        """Sets the chassis_code of this NodeHardwareNode.

        Chassis code of this node (1U, 2U, etc.).  # noqa: E501

        :param chassis_code: The chassis_code of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if chassis_code is not None and len(chassis_code) > 255:
            raise ValueError("Invalid value for `chassis_code`, length must be less than or equal to `255`")  # noqa: E501
        if chassis_code is not None and len(chassis_code) < 0:
            raise ValueError("Invalid value for `chassis_code`, length must be greater than or equal to `0`")  # noqa: E501

        self._chassis_code = chassis_code

    @property
    def chassis_count(self):
        """Gets the chassis_count of this NodeHardwareNode.  # noqa: E501

        Number of chassis making up this node.  # noqa: E501

        :return: The chassis_count of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self._chassis_count

    @chassis_count.setter
    def chassis_count(self, chassis_count):
        """Sets the chassis_count of this NodeHardwareNode.

        Number of chassis making up this node.  # noqa: E501

        :param chassis_count: The chassis_count of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if chassis_count is not None and len(chassis_count) > 255:
            raise ValueError("Invalid value for `chassis_count`, length must be less than or equal to `255`")  # noqa: E501
        if chassis_count is not None and len(chassis_count) < 0:
            raise ValueError("Invalid value for `chassis_count`, length must be greater than or equal to `0`")  # noqa: E501

        self._chassis_count = chassis_count

    @property
    def _class(self):
        """Gets the _class of this NodeHardwareNode.  # noqa: E501

        Class of this node (storage, accelerator, etc.).  # noqa: E501

        :return: The _class of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this NodeHardwareNode.

        Class of this node (storage, accelerator, etc.).  # noqa: E501

        :param _class: The _class of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if _class is not None and len(_class) > 255:
            raise ValueError("Invalid value for `_class`, length must be less than or equal to `255`")  # noqa: E501
        if _class is not None and len(_class) < 0:
            raise ValueError("Invalid value for `_class`, length must be greater than or equal to `0`")  # noqa: E501

        self.__class = _class

    @property
    def configuration_id(self):
        """Gets the configuration_id of this NodeHardwareNode.  # noqa: E501

        Node configuration ID.  # noqa: E501

        :return: The configuration_id of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """Sets the configuration_id of this NodeHardwareNode.

        Node configuration ID.  # noqa: E501

        :param configuration_id: The configuration_id of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if configuration_id is not None and len(configuration_id) > 255:
            raise ValueError("Invalid value for `configuration_id`, length must be less than or equal to `255`")  # noqa: E501
        if configuration_id is not None and len(configuration_id) < 0:
            raise ValueError("Invalid value for `configuration_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._configuration_id = configuration_id

    @property
    def cpu(self):
        """Gets the cpu of this NodeHardwareNode.  # noqa: E501

        Manufacturer and model of this node's CPU.  # noqa: E501

        :return: The cpu of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this NodeHardwareNode.

        Manufacturer and model of this node's CPU.  # noqa: E501

        :param cpu: The cpu of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if cpu is not None and len(cpu) > 255:
            raise ValueError("Invalid value for `cpu`, length must be less than or equal to `255`")  # noqa: E501
        if cpu is not None and len(cpu) < 0:
            raise ValueError("Invalid value for `cpu`, length must be greater than or equal to `0`")  # noqa: E501

        self._cpu = cpu

    @property
    def disk_controller(self):
        """Gets the disk_controller of this NodeHardwareNode.  # noqa: E501

        Manufacturer and model of this node's disk controller.  # noqa: E501

        :return: The disk_controller of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self._disk_controller

    @disk_controller.setter
    def disk_controller(self, disk_controller):
        """Sets the disk_controller of this NodeHardwareNode.

        Manufacturer and model of this node's disk controller.  # noqa: E501

        :param disk_controller: The disk_controller of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if disk_controller is not None and len(disk_controller) > 255:
            raise ValueError("Invalid value for `disk_controller`, length must be less than or equal to `255`")  # noqa: E501
        if disk_controller is not None and len(disk_controller) < 0:
            raise ValueError("Invalid value for `disk_controller`, length must be greater than or equal to `0`")  # noqa: E501

        self._disk_controller = disk_controller

    @property
    def disk_expander(self):
        """Gets the disk_expander of this NodeHardwareNode.  # noqa: E501

        Manufacturer and model of this node's disk expander.  # noqa: E501

        :return: The disk_expander of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self._disk_expander

    @disk_expander.setter
    def disk_expander(self, disk_expander):
        """Sets the disk_expander of this NodeHardwareNode.

        Manufacturer and model of this node's disk expander.  # noqa: E501

        :param disk_expander: The disk_expander of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if disk_expander is not None and len(disk_expander) > 255:
            raise ValueError("Invalid value for `disk_expander`, length must be less than or equal to `255`")  # noqa: E501
        if disk_expander is not None and len(disk_expander) < 0:
            raise ValueError("Invalid value for `disk_expander`, length must be greater than or equal to `0`")  # noqa: E501

        self._disk_expander = disk_expander

    @property
    def family_code(self):
        """Gets the family_code of this NodeHardwareNode.  # noqa: E501

        Family code of this node (X, S, NL, etc.).  # noqa: E501

        :return: The family_code of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self._family_code

    @family_code.setter
    def family_code(self, family_code):
        """Sets the family_code of this NodeHardwareNode.

        Family code of this node (X, S, NL, etc.).  # noqa: E501

        :param family_code: The family_code of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if family_code is not None and len(family_code) > 255:
            raise ValueError("Invalid value for `family_code`, length must be less than or equal to `255`")  # noqa: E501
        if family_code is not None and len(family_code) < 0:
            raise ValueError("Invalid value for `family_code`, length must be greater than or equal to `0`")  # noqa: E501

        self._family_code = family_code

    @property
    def flash_drive(self):
        """Gets the flash_drive of this NodeHardwareNode.  # noqa: E501

        Manufacturer, model, and device id of this node's flash drive.  # noqa: E501

        :return: The flash_drive of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self._flash_drive

    @flash_drive.setter
    def flash_drive(self, flash_drive):
        """Sets the flash_drive of this NodeHardwareNode.

        Manufacturer, model, and device id of this node's flash drive.  # noqa: E501

        :param flash_drive: The flash_drive of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if flash_drive is not None and len(flash_drive) > 255:
            raise ValueError("Invalid value for `flash_drive`, length must be less than or equal to `255`")  # noqa: E501
        if flash_drive is not None and len(flash_drive) < 0:
            raise ValueError("Invalid value for `flash_drive`, length must be greater than or equal to `0`")  # noqa: E501

        self._flash_drive = flash_drive

    @property
    def generation_code(self):
        """Gets the generation_code of this NodeHardwareNode.  # noqa: E501

        Generation code of this node.  # noqa: E501

        :return: The generation_code of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self._generation_code

    @generation_code.setter
    def generation_code(self, generation_code):
        """Sets the generation_code of this NodeHardwareNode.

        Generation code of this node.  # noqa: E501

        :param generation_code: The generation_code of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if generation_code is not None and len(generation_code) > 255:
            raise ValueError("Invalid value for `generation_code`, length must be less than or equal to `255`")  # noqa: E501
        if generation_code is not None and len(generation_code) < 0:
            raise ValueError("Invalid value for `generation_code`, length must be greater than or equal to `0`")  # noqa: E501

        self._generation_code = generation_code

    @property
    def hwgen(self):
        """Gets the hwgen of this NodeHardwareNode.  # noqa: E501

        PowerScale hardware generation name.  # noqa: E501

        :return: The hwgen of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self._hwgen

    @hwgen.setter
    def hwgen(self, hwgen):
        """Sets the hwgen of this NodeHardwareNode.

        PowerScale hardware generation name.  # noqa: E501

        :param hwgen: The hwgen of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if hwgen is not None and len(hwgen) > 255:
            raise ValueError("Invalid value for `hwgen`, length must be less than or equal to `255`")  # noqa: E501
        if hwgen is not None and len(hwgen) < 0:
            raise ValueError("Invalid value for `hwgen`, length must be greater than or equal to `0`")  # noqa: E501

        self._hwgen = hwgen

    @property
    def id(self):
        """Gets the id of this NodeHardwareNode.  # noqa: E501

        Node ID (Device Number) of a node.  # noqa: E501

        :return: The id of this NodeHardwareNode.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeHardwareNode.

        Node ID (Device Number) of a node.  # noqa: E501

        :param id: The id of this NodeHardwareNode.  # noqa: E501
        :type: int
        """
        if id is not None and id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if id is not None and id < 0:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def imb_version(self):
        """Gets the imb_version of this NodeHardwareNode.  # noqa: E501

        Version of this node's PowerScale Management Board.  # noqa: E501

        :return: The imb_version of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self._imb_version

    @imb_version.setter
    def imb_version(self, imb_version):
        """Sets the imb_version of this NodeHardwareNode.

        Version of this node's PowerScale Management Board.  # noqa: E501

        :param imb_version: The imb_version of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if imb_version is not None and len(imb_version) > 255:
            raise ValueError("Invalid value for `imb_version`, length must be less than or equal to `255`")  # noqa: E501
        if imb_version is not None and len(imb_version) < 0:
            raise ValueError("Invalid value for `imb_version`, length must be greater than or equal to `0`")  # noqa: E501

        self._imb_version = imb_version

    @property
    def infiniband(self):
        """Gets the infiniband of this NodeHardwareNode.  # noqa: E501

        Infiniband card type.  # noqa: E501

        :return: The infiniband of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self._infiniband

    @infiniband.setter
    def infiniband(self, infiniband):
        """Sets the infiniband of this NodeHardwareNode.

        Infiniband card type.  # noqa: E501

        :param infiniband: The infiniband of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if infiniband is not None and len(infiniband) > 255:
            raise ValueError("Invalid value for `infiniband`, length must be less than or equal to `255`")  # noqa: E501
        if infiniband is not None and len(infiniband) < 0:
            raise ValueError("Invalid value for `infiniband`, length must be greater than or equal to `0`")  # noqa: E501

        self._infiniband = infiniband

    @property
    def lcd_version(self):
        """Gets the lcd_version of this NodeHardwareNode.  # noqa: E501

        Version of the LCD panel.  # noqa: E501

        :return: The lcd_version of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self._lcd_version

    @lcd_version.setter
    def lcd_version(self, lcd_version):
        """Sets the lcd_version of this NodeHardwareNode.

        Version of the LCD panel.  # noqa: E501

        :param lcd_version: The lcd_version of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if lcd_version is not None and len(lcd_version) > 255:
            raise ValueError("Invalid value for `lcd_version`, length must be less than or equal to `255`")  # noqa: E501
        if lcd_version is not None and len(lcd_version) < 0:
            raise ValueError("Invalid value for `lcd_version`, length must be greater than or equal to `0`")  # noqa: E501

        self._lcd_version = lcd_version

    @property
    def lnn(self):
        """Gets the lnn of this NodeHardwareNode.  # noqa: E501

        Logical Node Number (LNN) of a node.  # noqa: E501

        :return: The lnn of this NodeHardwareNode.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this NodeHardwareNode.

        Logical Node Number (LNN) of a node.  # noqa: E501

        :param lnn: The lnn of this NodeHardwareNode.  # noqa: E501
        :type: int
        """
        if lnn is not None and lnn > 65535:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `65535`")  # noqa: E501
        if lnn is not None and lnn < 1:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._lnn = lnn

    @property
    def motherboard(self):
        """Gets the motherboard of this NodeHardwareNode.  # noqa: E501

        Manufacturer and model of this node's motherboard.  # noqa: E501

        :return: The motherboard of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self._motherboard

    @motherboard.setter
    def motherboard(self, motherboard):
        """Sets the motherboard of this NodeHardwareNode.

        Manufacturer and model of this node's motherboard.  # noqa: E501

        :param motherboard: The motherboard of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if motherboard is not None and len(motherboard) > 255:
            raise ValueError("Invalid value for `motherboard`, length must be less than or equal to `255`")  # noqa: E501
        if motherboard is not None and len(motherboard) < 0:
            raise ValueError("Invalid value for `motherboard`, length must be greater than or equal to `0`")  # noqa: E501

        self._motherboard = motherboard

    @property
    def net_interfaces(self):
        """Gets the net_interfaces of this NodeHardwareNode.  # noqa: E501

        Description of all this node's network interfaces.  # noqa: E501

        :return: The net_interfaces of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self._net_interfaces

    @net_interfaces.setter
    def net_interfaces(self, net_interfaces):
        """Sets the net_interfaces of this NodeHardwareNode.

        Description of all this node's network interfaces.  # noqa: E501

        :param net_interfaces: The net_interfaces of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if net_interfaces is not None and len(net_interfaces) > 255:
            raise ValueError("Invalid value for `net_interfaces`, length must be less than or equal to `255`")  # noqa: E501
        if net_interfaces is not None and len(net_interfaces) < 0:
            raise ValueError("Invalid value for `net_interfaces`, length must be greater than or equal to `0`")  # noqa: E501

        self._net_interfaces = net_interfaces

    @property
    def nvram(self):
        """Gets the nvram of this NodeHardwareNode.  # noqa: E501

        Manufacturer and model of this node's NVRAM board.  # noqa: E501

        :return: The nvram of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self._nvram

    @nvram.setter
    def nvram(self, nvram):
        """Sets the nvram of this NodeHardwareNode.

        Manufacturer and model of this node's NVRAM board.  # noqa: E501

        :param nvram: The nvram of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if nvram is not None and len(nvram) > 255:
            raise ValueError("Invalid value for `nvram`, length must be less than or equal to `255`")  # noqa: E501
        if nvram is not None and len(nvram) < 0:
            raise ValueError("Invalid value for `nvram`, length must be greater than or equal to `0`")  # noqa: E501

        self._nvram = nvram

    @property
    def powersupplies(self):
        """Gets the powersupplies of this NodeHardwareNode.  # noqa: E501

        Description strings for each power supply on this node.  # noqa: E501

        :return: The powersupplies of this NodeHardwareNode.  # noqa: E501
        :rtype: list[str]
        """
        return self._powersupplies

    @powersupplies.setter
    def powersupplies(self, powersupplies):
        """Sets the powersupplies of this NodeHardwareNode.

        Description strings for each power supply on this node.  # noqa: E501

        :param powersupplies: The powersupplies of this NodeHardwareNode.  # noqa: E501
        :type: list[str]
        """

        self._powersupplies = powersupplies

    @property
    def processor(self):
        """Gets the processor of this NodeHardwareNode.  # noqa: E501

        Number of processors and cores on this node.  # noqa: E501

        :return: The processor of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self._processor

    @processor.setter
    def processor(self, processor):
        """Sets the processor of this NodeHardwareNode.

        Number of processors and cores on this node.  # noqa: E501

        :param processor: The processor of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if processor is not None and len(processor) > 255:
            raise ValueError("Invalid value for `processor`, length must be less than or equal to `255`")  # noqa: E501
        if processor is not None and len(processor) < 0:
            raise ValueError("Invalid value for `processor`, length must be greater than or equal to `0`")  # noqa: E501

        self._processor = processor

    @property
    def product(self):
        """Gets the product of this NodeHardwareNode.  # noqa: E501

        PowerScale product name.  # noqa: E501

        :return: The product of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this NodeHardwareNode.

        PowerScale product name.  # noqa: E501

        :param product: The product of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if product is not None and len(product) > 255:
            raise ValueError("Invalid value for `product`, length must be less than or equal to `255`")  # noqa: E501
        if product is not None and len(product) < 0:
            raise ValueError("Invalid value for `product`, length must be greater than or equal to `0`")  # noqa: E501

        self._product = product

    @property
    def ram(self):
        """Gets the ram of this NodeHardwareNode.  # noqa: E501

        Size of RAM in bytes.  # noqa: E501

        :return: The ram of this NodeHardwareNode.  # noqa: E501
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this NodeHardwareNode.

        Size of RAM in bytes.  # noqa: E501

        :param ram: The ram of this NodeHardwareNode.  # noqa: E501
        :type: int
        """
        if ram is not None and ram > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `ram`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if ram is not None and ram < 0:  # noqa: E501
            raise ValueError("Invalid value for `ram`, must be a value greater than or equal to `0`")  # noqa: E501

        self._ram = ram

    @property
    def serial_number(self):
        """Gets the serial_number of this NodeHardwareNode.  # noqa: E501

        Serial number of this node.  # noqa: E501

        :return: The serial_number of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this NodeHardwareNode.

        Serial number of this node.  # noqa: E501

        :param serial_number: The serial_number of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if serial_number is not None and len(serial_number) > 255:
            raise ValueError("Invalid value for `serial_number`, length must be less than or equal to `255`")  # noqa: E501
        if serial_number is not None and len(serial_number) < 0:
            raise ValueError("Invalid value for `serial_number`, length must be greater than or equal to `0`")  # noqa: E501

        self._serial_number = serial_number

    @property
    def series(self):
        """Gets the series of this NodeHardwareNode.  # noqa: E501

        Series of this node (X, I, NL, etc.).  # noqa: E501

        :return: The series of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this NodeHardwareNode.

        Series of this node (X, I, NL, etc.).  # noqa: E501

        :param series: The series of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if series is not None and len(series) > 255:
            raise ValueError("Invalid value for `series`, length must be less than or equal to `255`")  # noqa: E501
        if series is not None and len(series) < 0:
            raise ValueError("Invalid value for `series`, length must be greater than or equal to `0`")  # noqa: E501

        self._series = series

    @property
    def storage_class(self):
        """Gets the storage_class of this NodeHardwareNode.  # noqa: E501

        Storage class of this node (storage or diskless).  # noqa: E501

        :return: The storage_class of this NodeHardwareNode.  # noqa: E501
        :rtype: str
        """
        return self._storage_class

    @storage_class.setter
    def storage_class(self, storage_class):
        """Sets the storage_class of this NodeHardwareNode.

        Storage class of this node (storage or diskless).  # noqa: E501

        :param storage_class: The storage_class of this NodeHardwareNode.  # noqa: E501
        :type: str
        """
        if storage_class is not None and len(storage_class) > 255:
            raise ValueError("Invalid value for `storage_class`, length must be less than or equal to `255`")  # noqa: E501
        if storage_class is not None and len(storage_class) < 0:
            raise ValueError("Invalid value for `storage_class`, length must be greater than or equal to `0`")  # noqa: E501

        self._storage_class = storage_class

    @property
    def tier(self):
        """Gets the tier of this NodeHardwareNode.  # noqa: E501

        Platform tier level of this node if applicable (1-6 are defined, 0 for unknown or not supported, -1 for error). If not supported: 0. If Logic to determine tier fails: 0 for unknown. If PSI_Get fails: -1 for error. PSI_Get can fail if PSI not initialized, or key does not exist.  # noqa: E501

        :return: The tier of this NodeHardwareNode.  # noqa: E501
        :rtype: int
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """Sets the tier of this NodeHardwareNode.

        Platform tier level of this node if applicable (1-6 are defined, 0 for unknown or not supported, -1 for error). If not supported: 0. If Logic to determine tier fails: 0 for unknown. If PSI_Get fails: -1 for error. PSI_Get can fail if PSI not initialized, or key does not exist.  # noqa: E501

        :param tier: The tier of this NodeHardwareNode.  # noqa: E501
        :type: int
        """
        if tier is not None and tier > 6:  # noqa: E501
            raise ValueError("Invalid value for `tier`, must be a value less than or equal to `6`")  # noqa: E501
        if tier is not None and tier < -1:  # noqa: E501
            raise ValueError("Invalid value for `tier`, must be a value greater than or equal to `-1`")  # noqa: E501

        self._tier = tier

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NodeHardwareNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
