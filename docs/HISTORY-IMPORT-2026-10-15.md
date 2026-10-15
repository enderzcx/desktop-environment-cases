# 历史案例补录 · 2026-10-15

本轮将现有 BeefTV 桌面环境故障历史补入案例库。原有 2 条保留，新补 ENV-0003 至 ENV-0053 共 51 条；当前共 53 条，其中 48 条根因已确认、5 条待定位。状态确认的是案例中明确写出的机制，不代表发布或原客户恢复。

## 来源与核对范围

- 检查 glanderness/BeefTV 当时可见的全部 145 个 PR 标题，重点读取下表涉及的 42 个 PR 正文、合并状态和固定提交代码或验收记录。
- 回读公开 Issue [#103](https://github.com/glanderness/BeefTV/issues/103) 与 [#118](https://github.com/glanderness/BeefTV/issues/118) 及后续诊断回复；两项根因仍未知，保留 reported。
- 以 2026-10-15 的主线 e126cf93 和历史固定提交交叉核对。新案例的 46 个固定代码/资料路径均在对应提交存在；来源不是移动分支。
- 先用历史记忆检索定位线索，再以 PR、代码和原有验收资料为正式案例来源。原始客户聊天、截图、诊断 ZIP、姓名、账号和机器路径未入库。
- 后续通过定向记忆定位并读取了原有 18 项群反馈审计表。本轮只提取脱敏症状，并逐项对应如下；原表的“全部根治”等结论不是验收依据，仍以原请求、代码和具体历史验证为准。原表含客户身份和本机路径，未上传。

## 收录索引

| 案例 | 内容 | 主要来源 |
| --- | --- | --- |
| [ENV-0003](cases/ENV-0003.md) | 减少动态效果使模型菜单定位到视口外 | [PR #137](https://github.com/glanderness/BeefTV/pull/137) |
| [ENV-0004](cases/ENV-0004.md) | Windows 安装目录重命名遇到共享冲突或错误 32 | [PR #151](https://github.com/glanderness/BeefTV/pull/151) |
| [ENV-0005](cases/ENV-0005.md) | 英文构建机把 NSIS 中文提示编译成乱码 | [PR #151](https://github.com/glanderness/BeefTV/pull/151) |
| [ENV-0006](cases/ENV-0006.md) | 运行中的临时文件阻止整个存储目录迁移 | [PR #126](https://github.com/glanderness/BeefTV/pull/126) |
| [ENV-0007](cases/ENV-0007.md) | 迁移或重启后数据目录发现错误导致工作区看似丢失 | [PR #116](https://github.com/glanderness/BeefTV/pull/116) |
| [ENV-0008](cases/ENV-0008.md) | 本地凭据文件读取或解密失败被误报为模型参数错误 | [PR #157](https://github.com/glanderness/BeefTV/pull/157) |
| [ENV-0009](cases/ENV-0009.md) | 本地磁盘写满导致生成结果保存或取回失败 | [PR #157](https://github.com/glanderness/BeefTV/pull/157) |
| [ENV-0010](cases/ENV-0010.md) | 桌面启动未继承终端代理导致更新或组件下载失败 | [PR #18](https://github.com/glanderness/BeefTV/pull/18) |
| [ENV-0011](cases/ENV-0011.md) | 本地深度子进程补下载模型时没有继承桌面代理 | [PR #142](https://github.com/glanderness/BeefTV/pull/142) |
| [ENV-0012](cases/ENV-0012.md) | PowerShell 生成的 ZIP 使用反斜杠条目被解压器拒绝 | [PR #47](https://github.com/glanderness/BeefTV/pull/47) |
| [ENV-0013](cases/ENV-0013.md) | PowerShell 5.1 提前关闭输出管道使正常工具自检失败 | [PR #45](https://github.com/glanderness/BeefTV/pull/45) |
| [ENV-0014](cases/ENV-0014.md) | Windows 无法解码 HEVC 且缺少可用 FFmpeg 预览工具 | [PR #105](https://github.com/glanderness/BeefTV/pull/105) |
| [ENV-0015](cases/ENV-0015.md) | 构建目录已有媒体运行时但最终更新 ZIP 漏装 | [PR #106](https://github.com/glanderness/BeefTV/pull/106) |
| [ENV-0016](cases/ENV-0016.md) | 已发布旧更新器拒绝新增 CLI 或媒体目录 | [PR #111](https://github.com/glanderness/BeefTV/pull/111) |
| [ENV-0017](cases/ENV-0017.md) | Windows 原生连接重置未被识别导致任务提前失败 | [PR #56](https://github.com/glanderness/BeefTV/pull/56) |
| [ENV-0018](cases/ENV-0018.md) | macOS 首次安装被 Gatekeeper 拦截而更新清单验签正常 | [PR #27](https://github.com/glanderness/BeefTV/pull/27) |
| [ENV-0019](cases/ENV-0019.md) | AppData 影子文件与运行时发现路径冲突（MSIX 待实测） | [PR #70](https://github.com/glanderness/BeefTV/pull/70) |
| [ENV-0020](cases/ENV-0020.md) | Windows 发布包漏装 CLI 使 MCP 错启动桌面主程序 | [PR #70](https://github.com/glanderness/BeefTV/pull/70) |
| [ENV-0021](cases/ENV-0021.md) | Windows GUI 启动 Node 助手时出现额外黑色控制台 | [PR #70](https://github.com/glanderness/BeefTV/pull/70) |
| [ENV-0022](cases/ENV-0022.md) | 成功升级后的暂存目录长期累积占用磁盘 | [PR #69](https://github.com/glanderness/BeefTV/pull/69) |
| [ENV-0023](cases/ENV-0023.md) | 慢线路下载被总时长上限打断且不能续传 | [PR #80](https://github.com/glanderness/BeefTV/pull/80) |
| [ENV-0024](cases/ENV-0024.md) | Windows 在只读下载句柄上 Sync 导致校验后失败 | [PR #83](https://github.com/glanderness/BeefTV/pull/83) |
| [ENV-0025](cases/ENV-0025.md) | SQLite 本地时区时间与 UTC 字符串比较使诊断包漏采 | [PR #127](https://github.com/glanderness/BeefTV/pull/127) |
| [ENV-0026](cases/ENV-0026.md) | 旧预览数据库迁移编号冲突导致正式版缺列 | [PR #55](https://github.com/glanderness/BeefTV/pull/55) |
| [ENV-0027](cases/ENV-0027.md) | Windows 原生保存框改名后丢失媒体扩展名 | [PR #59](https://github.com/glanderness/BeefTV/pull/59) |
| [ENV-0028](cases/ENV-0028.md) | 低速本地深度处理超过前端等待时间被提前判失败 | [PR #142](https://github.com/glanderness/BeefTV/pull/142) |
| [ENV-0029](cases/ENV-0029.md) | 远端视频取帧的凭据策略与解码能力不匹配 | [PR #153](https://github.com/glanderness/BeefTV/pull/153) |
| [ENV-0030](cases/ENV-0030.md) | 浅色 Windows 系统主题让深色桌面应用出现白色标题栏 | [PR #153](https://github.com/glanderness/BeefTV/pull/153) |
| [ENV-0031](cases/ENV-0031.md) | 续传重置缓存失败后旧字节与新标识混用 | [PR #154](https://github.com/glanderness/BeefTV/pull/154) |
| [ENV-0032](cases/ENV-0032.md) | 弱 ETag 或仅 Last-Modified 不足以保证断点字节属于同一对象 | [PR #154](https://github.com/glanderness/BeefTV/pull/154) |
| [ENV-0033](cases/ENV-0033.md) | 发布机 Bun 版本不支持已提交锁文件格式 | [PR #66](https://github.com/glanderness/BeefTV/pull/66) |
| [ENV-0034](cases/ENV-0034.md) | Windows CI 固定 MSYS2 路径与 Action 实际安装位置不同 | [PR #14](https://github.com/glanderness/BeefTV/pull/14) |
| [ENV-0035](cases/ENV-0035.md) | Intel Mac 发布误用 ARM runner 造成双架构参数冲突 | [PR #14](https://github.com/glanderness/BeefTV/pull/14) |
| [ENV-0036](cases/ENV-0036.md) | 图片读取或解码失败被画布显示成透明空节点 | [PR #138](https://github.com/glanderness/BeefTV/pull/138) |
| [ENV-0037](cases/ENV-0037.md) | 第三方批量生图上游成功而本地结果未知（待定位） | [Issue #118](https://github.com/glanderness/BeefTV/issues/118) |
| [ENV-0038](cases/ENV-0038.md) | Windows 图片二次处理出现空指针 panic（待复现） | [Issue #103](https://github.com/glanderness/BeefTV/issues/103) |
| [ENV-0039](cases/ENV-0039.md) | 更新下载完成后准备阶段超时（具体瓶颈待定位） | [PR #158](https://github.com/glanderness/BeefTV/pull/158) |
| [ENV-0040](cases/ENV-0040.md) | 更新准备重复解压并刷盘使低速磁盘等待放大 | [PR #136](https://github.com/glanderness/BeefTV/pull/136) |
| [ENV-0041](cases/ENV-0041.md) | 模型目录很大时重复线性查找造成选择框长时间阻塞 | [PR #127](https://github.com/glanderness/BeefTV/pull/127) |
| [ENV-0042](cases/ENV-0042.md) | 原生 WebView 的本地模型中转预检缺少允许请求头 | [PR #63](https://github.com/glanderness/BeefTV/pull/63) |
| [ENV-0043](cases/ENV-0043.md) | macOS 视频元素全屏 | [PR #133](https://github.com/glanderness/BeefTV/pull/133) |
| [ENV-0044](cases/ENV-0044.md) | 生成结果慢速下载与过早绑定 | [PR #123](https://github.com/glanderness/BeefTV/pull/123) |
| [ENV-0045](cases/ENV-0045.md) | 视频结果路线停滞与签名恢复 | [PR #146](https://github.com/glanderness/BeefTV/pull/146) |
| [ENV-0046](cases/ENV-0046.md) | 同进程并发首次安装共写组件缓存 | [PR #44](https://github.com/glanderness/BeefTV/pull/44) |
| [ENV-0047](cases/ENV-0047.md) | PowerShell 5.1 源脚本编码 | [PR #44](https://github.com/glanderness/BeefTV/pull/44) |
| [ENV-0048](cases/ENV-0048.md) | 低帧率时长校验容差 | [PR #44](https://github.com/glanderness/BeefTV/pull/44) |
| [ENV-0049](cases/ENV-0049.md) | 隔离工作区缺少 Node 宿主依赖 | [PR #156](https://github.com/glanderness/BeefTV/pull/156) |
| [ENV-0050](cases/ENV-0050.md) | MP4 使用通用二进制 MIME | [PR #146](https://github.com/glanderness/BeefTV/pull/146) |
| [ENV-0051](cases/ENV-0051.md) | 多视频画布平移的渲染负载 | [PR #149](https://github.com/glanderness/BeefTV/pull/149) |
| [ENV-0052](cases/ENV-0052.md) | 重启换端口后 MCP 地址失效 | [PR #115](https://github.com/glanderness/BeefTV/pull/115) |
| [ENV-0053](cases/ENV-0053.md) | HTTP 415 历史报告待核对 | [PR #144](https://github.com/glanderness/BeefTV/pull/144)（仅关联实现） |

## 18 项群反馈逐项去向

| 原表项 | 去向 |
| --- | --- |
| 已修复表 1：生成后卡在取回 | ENV-0031、0032、0044、0045；不继承原表对所有现场“根治”的说法 |
| 已修复表 2：复制节点新生成仍显示旧视频 | 普通画布状态与结果绑定逻辑，未证实环境关联，不作为环境根因入库 |
| 已修复表 3：多视频画布卡顿 | ENV-0051 |
| 已修复表 4：默认模型无法选择 | ENV-0003、0041；两种根因分别验证 |
| 已修复表 5：深度超时及重启残留错误 | ENV-0011、0028 |
| 已修复表 6：H3 首尾帧比例 | 供应商能力与产品提示合同，未证实环境关联 |
| 已修复表 7：Windows 图片透明 | ENV-0036；首次读取诱因仍未知，展示机制已确认 |
| 已修复表 8：HTTP 415 | ENV-0053，保留 reported，不依据相邻协议修复直接关闭 |
| 已修复表 9：全屏/H3 设置按钮 | 元素全屏进 ENV-0043；H3 设置入口属于普通 UI 问题 |
| 已修复表 10：WorkBuddy/DSH MCP 连接失败 | ENV-0052；实际采用 #115 的调用前发现，不照搬已关闭 #87 的失败后重放草案 |
| 已修复表 11：图片参数/比例不可选 | 模型档案与协议配置，未证明是系统环境原因 |
| 已修复表 12：Windows 更新安装失败 | ENV-0004、0016、0023、0024、0039、0040，按阶段区分 |
| 功能/边界表 1：图片改名入口 | 已有操作入口与缩放条件；保留为使用说明，不虚构为环境故障 |
| 功能/边界表 2：某上游提交失败/长时间等待 | 原表没有服务日志或原请求，不继承“上游宕机”定论；不归为本机环境根因 |
| 功能/边界表 3：换电脑后无原项目 | 本地项目存储与算力账号登录是不同能力；不是已证实丢失，不自动承诺云同步 |
| 功能/边界表 4：双品牌 API 配置 | 接入说明，未提供环境故障 |
| 后续修复表 1：远端视频取帧 | ENV-0029；未把尾帧时间计算混作环境问题 |
| 后续修复表 2：Windows 白色标题栏 | ENV-0030 |

## 合并与排除

- PR #18、#47、#104 的父进程系统代理遗漏集中到 ENV-0010；Python/curl 子进程继承是另一条调用链，保留 ENV-0011。
- PR #74 与 #111 的旧更新器布局限制集中到 ENV-0016，并写明不同旧版本允许目录不同；CLI 本身漏装另列 ENV-0020，媒体归档漏装另列 ENV-0015。
- 文件锁导致的安装替换失败（ENV-0004）与临时文件阻止数据迁移（ENV-0006）处理对象不同，分别保留；不把持久素材也视作可跳过临时数据。
- 菜单离屏（ENV-0003）与大模型目录计算卡顿（ENV-0041）分别有证据，不能相互替代。未采纳的全局 0s 过渡方案只作为风险说明，不虚构成客户案例。
- 更新准备超时未定位（ENV-0039）与已确认的重复解压（ENV-0040）分开。PR #158 的诊断改进不能标记原超时根治。
- 无法确认结果的批量生图（ENV-0037）、空指针报告（ENV-0038）与 HTTP 415 报告（ENV-0053）保留症状和后续验证条件，未推定为断网、并发、WebView 或磁盘问题。
- 单纯新功能、渠道命名、供应商协议/参数适配、计费、画布编辑业务逻辑等没有证实环境关联的变化未填入环境案例。PR #153 的尾帧时间计算与平台媒体/CORS、标题栏问题分开看；前者没有被冒充环境故障。
- Linux WebKitGTK 依赖清单、CUDA 社区预览与未验证发行版属于支持范围/待验收能力；没有用“可能不兼容”虚构已发生的故障。
- 外部服务/供应商失败和历史服务器运维问题不因发生在同一产品中就收录为桌面环境根因。

## 本轮验证的含义

运行案例 schema、引用和状态校验、生成文件一致性、未知平台检索以及现有缺失 API 最小复现。未重新执行历史付费调用、原生升级/回滚、客户机器操作或全部跨平台矩阵；具体历史执行范围保留在各条证据和限制里。

新补条目不附造假的“本库已复现”标签。案例中的复检步骤用于未来重放，当前已执行的独立夹具仍只有 ENV-0001。
