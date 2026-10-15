# 行业参考

查阅日期：2026-10-15。以下是研究入口，不是已经在某个客户机器上验证的修复方案。

| 项目 | 可复用部分 | 限制 |
| --- | --- | --- |
| [MDN browser-compat-data](https://github.com/mdn/browser-compat-data) | 网页 API 和浏览器版本兼容数据，数据许可 CC0 | 不记录驱动、企业策略、磁盘和网络故障 |
| [eslint-plugin-es-x](https://eslint-community.github.io/eslint-plugin-es-x/rules/no-array-prototype-tosorted.html) | ECMAScript API 使用检查 | 实例方法规则可能默认静默，需要类型信息或明确配置，并以负例验证 |
| [WebView2 部署文档](https://learn.microsoft.com/en-us/microsoft-edge/webview2/concepts/distribution) | 运行时检测、在线/离线安装、更新后重启 | 安装版本、可用版本与进程当前使用的版本要分别核实 |
| [WebView2Feedback](https://github.com/MicrosoftEdge/WebView2Feedback) | 上游已知故障、复现与讨论 | 相同症状不等于相同根因 |
| [Chromium GPU 问题清单](https://chromium.googlesource.com/chromium/src/+/main/gpu/config/gpu_driver_bug_list.json) | 驱动问题与平台条件 | 规则与引擎版本绑定，需在目标产品复验 |
| [Replicated Troubleshoot](https://troubleshoot.sh/docs/host-collect-analyze/overview/) | 采集、脱敏、支持包和规则分析；Apache-2.0 | 主要面向服务器/Kubernetes；host collectors 本身可不依赖 Kubernetes |
| [gopsutil](https://github.com/shirou/gopsutil) | Go 系统信息采集 | 系统参数不能替代功能实测，各平台字段支持不同 |
| [VS Code FAQ](https://code.visualstudio.com/docs/supporting/faq#_vs-code-is-blank) | GPU 故障的诊断与降级经验 | 软件渲染会影响性能，不能自动套用到所有空白窗口 |
| [Tauri WebView 版本说明](https://v2.tauri.app/reference/webview-versions/) | Windows/macOS/Linux 引擎来源与差异 | 版本映射需要随系统更新重新核对 |
| [WebKitGTK 媒体文档](https://docs.webkit.org/Ports/WebKitGTK%20and%20WPE%20WebKit/Multimedia.html) | GStreamer 媒体依赖 | 安装 WebKitGTK 不等于所有媒体格式都可播放 |

这些来源按领域积累知识。进入案例库时，需要补上目标环境、实际症状、证据和复检方法。
