CREATE TABLE `china_post_office` (  
    `sheng` VARCHAR(255) NOT NULL,      -- 省份  
    `shi` VARCHAR(255) NOT NULL,        -- 城市  
    `xian` VARCHAR(255) NOT NULL,       -- 县/区  
    `name` VARCHAR(255) NOT NULL,       -- 邮局名称  
    `post_code` VARCHAR(6) NOT NULL,    -- 邮政编码  
    `address` VARCHAR(255) NOT NULL,    -- 地址  
    `finance` ENUM('是', '否') NOT NULL, -- 是否提供金融服务，这里使用ENUM类型  
    `phone` VARCHAR(20) NOT NULL,       -- 电话  
    `time_s` VARCHAR(255) NOT NULL,       -- 星期几营业
    `time_h` VARCHAR(255) NOT NULL        -- 营业时间,几点到几点  
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;  -- 假设使用InnoDB存储引擎和utf8mb4字符集