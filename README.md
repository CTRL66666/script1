"""
本脚本用于Windows电脑自动连接预设好的校园网公共Wifi,可以实现开机自动连接、检测断开自动重连等功能,帮助电脑在校园网覆盖范围内实现校园网常驻在线。以下是该脚本详细使用说明：

一、使用步骤:
1. 运行软件
   - 运行程序进入主页面

2. 首次配置
   - 运行程序后输入校园网账号/密码
   - 选择运营商（电信/移动）
   - 点击【保存配置】存储登录凭证4

3. 功能操作
   - 启动脚本：点击【启动脚本】开始自动检测网络状态
   - 后台运行：通过【设置】启用托盘最小化功能
   - 高级设置：
     * 调整检测周期（默认20秒）
     * 设置最大重连次数（默认10次）
     * 启用Wifi自动切换

4. 系统集成
   - 在设置中勾选【开机自启动】创建启动项快捷方式
   - 启用【默认启动时运行工具】实现无感自动连接

二、注意事项:
1. 网络环境
   - 需确保电脑支持WLAN无线连接,台式电脑需要无线网卡
   - 校园网SSID必须包含"JXUST-WLAN"

2. 异常处理
   - 遇到连接失败时检查账号运营商是否匹配
   - 频繁断连可尝试缩短检测周期（最低0.5秒）
   - 系统休眠唤醒后会自动恢复检测线程
   - 部分笔记本机型如天选、华硕等勾选用户级自启动后程序可能会被检测并拉黑
   - 解决方法：1.添加信任；2.手动添加自启动
   - 若检查更新失败，请尝试访问github代码仓获取最新版本
     

3. 安全提示
   - 密码输入框默认隐藏，通过【密码显示】按钮临时查看
   - 该程序只向您的校园网发送登录请求及访问github查看最新日志,不涉及更多网络请求
   - 本程序所有数据均保存于本地,请注意保护密码隐私

4. 特殊功能
   - 调试模式可查看实时日志和网络状态
   - 支持通过右下角弹窗提示连接状态
   - 内置防IP冲突机制和证书验证模块

三、技术特性:
1. 采用tkinter实现Python跨版本GUI兼容
2. 集成requests会话保持和智能重试机制
3. 实现系统唤醒事件监听
4. 内存优化设计（常驻内存<50MB）

四、最后:
1. 该软件不对校园网IP频繁发送网络请求,网络测试均在本地进行
2. 绿色免费开源软件,请勿用作其他用途
3. 建议定期检查更新获取更稳定版本
4. 程序仍有许多地方存在不足,感谢您的提出建议和批评

版本：v1.0.1 | 最后更新：2025-04-06
"""
