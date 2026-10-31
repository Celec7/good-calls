# Good Calls

**面向 Coding Agent 的软件工程判断力。**

*好的代码，始于好的判断。*
*更少繁文缛节，更多理性决策。*

[![skills.sh](https://skills.sh/b/Celec7/good-calls)](https://skills.sh/Celec7/good-calls)

一组经过实际开发经验筛选、由 Agent 按需调用、旨在改善软件工程判断的十九个独立技能。原名 Beyond Code。

[English](README.md) | 中文

## 为什么需要这个项目

随着模型能力的持续增强，编写出极少语法或算法 bug 的代码已不再困难。但生成可运行的代码，并不等同于完成软件工程交付。

在用户初始且往往模糊的需求与可靠交付的软件之间，始终存在一条显著的软件工程鸿沟：

- 在动工之前理清真实问题与范围，而不是盲目猜测用户意图；
- 将复杂变更拆解为可独立验证的切片，而非堆积高风险的单体修改；
- 凭借系统化证据排查问题根因，而非治标不治本的修补；
- 权衡何时应当引入抽象，何时应保持简单；
- 辨别测试断言是提供了真实的行之有效的证明，还是仅仅带来了表面的虚假安全感；
- 记录无法从最终代码推导出的架构取舍与决策背景。

在通向通用人工智能的演进过程中，模型尚无法单纯通过预测下一个 Token 来弥合这种软件工程层面的断层。开发者作为人机协同中的核心中间层，关键责任就是打通从需求到交付的完整路径。

Good Calls 的定位是作为开发者的辅助工程工具：在关键决策点为 Agent 与开发者提供沉淀自实践的判断方法，而不是接管开发流程，更不是要求所有任务都服从一套机械的仪式。

## 设计哲学

### 更少繁文缛节，更多理性决策

高质量的软件源于严谨的工程取舍，而非对繁琐流程的顺从。指令保持直接、模块化且边界清晰。套件不设置强制的前置钩子、中心化路由技能或固定的调用链条。

### 技能的价值在于改变决策

一条软件工程原则只有在它能实质性改善 Agent 的具体决策时，才值得写进技能：何时提问、如何拆分、什么证据可信，以及哪些理由必须保留。如果模型原生就能稳定做好一项判断，重复灌输只会徒增上下文负担。

### 辅助引导，而非接管工作流

Agent 与开发者应当保留对开发过程的完全自主权。一个简单的单行修补，绝不应该仅仅因为安装了技能库，就被迫经历需求草案、形式化计划、多角色审查与归档记录等整套流程。不加载任何技能往往也是正确的决策。

### 避免上下文与协议污染

在早期的迭代中，项目曾尝试过严格的阶段门禁、任务台账与偏差阈值。实践表明，这些机制极易分散 Agent 的核心注意力。当 Agent 将大量的上下文预算消耗在记录框架状态、同步台账文件和证明自己符合流程规范上时，代码本身的质量与架构的可维护性反而被边缘化了。Good Calls 坚决精简流程负担，任务临时状态只保留在正常的对话上下文中。

### 面向能力更强的模型演进

随着基座模型推理能力的提升，技能不应固化过去为弥补模型缺陷而设的操作规程。模型越强，技能越应聚焦于难以自动推导的高价值工程取舍与边界判断，将具体的操作步骤留给模型的原生能力。

关于项目历史演化细节与对照实验记录，请参阅 [docs/design-philosophy.md](docs/design-philosophy.md)。

## 是什么与不是什么

- **它是**一组独立、按需调用的工程判断技能，涵盖需求澄清、架构设计、任务拆分、代码调试、可靠测试、审查及文档等维度。
- **它不是**刚性的软件开发工作流引擎或生命周期编排器。
- **它不是**多 Agent 蜂群编排系统或后台调度服务。
- **它不是**基于文件的 CLI 状态管理协议或任务台账系统。
- **它不是**面面俱到的软件工程理论百科全书。

## 技能目录

调用方式说明：
- **自主**：Agent 可以在适用场景下自主识别并选择，开发者也可随时显式调用。
- **仅用户**：用于对话模式的显式切换，必须由用户主动发起。

### 基础（Foundation）

基础技能承载被其他技能复用的底层工程判断。

| 技能 | 提供的判断 | 调用方式 |
| --- | --- | --- |
| [skill-authoring](skills/skill-authoring/SKILL.md) | 判断技能何时值得存在，并编写其描述、正文与测试 | 自主 |
| [error-handling](skills/error-handling/SKILL.md) | 定义失败、其归属者，以及失败后仍安全的部分 | 自主 |
| [prose-standard](skills/prose-standard/SKILL.md) | 保留每个命题，并规定各类散文必须说明什么 | 自主 |
| [trim-reasoning-leakage](skills/trim-reasoning-leakage/SKILL.md) | 清除以创作会话为视角的散文痕迹 | 自主 |

### 领域（Domain）

领域技能提供贯穿典型软件开发阶段的工程判断方法。

| 技能 | 提供的判断 | 调用方式 |
| --- | --- | --- |
| [clarify](skills/clarify/SKILL.md) | 澄清问题、结果和范围中的关键歧义 | 自主 |
| [codebase-design](skills/codebase-design/SKILL.md) | 安排责任与复杂性，设计有用的接口 | 自主 |
| [plan](skills/plan/SKILL.md) | 组织可验证切片、依赖与分阶段迁移 | 自主 |
| [tdd](skills/tdd/SKILL.md) | 一次一个行为，建立红绿重构循环 | 自主 |
| [debug](skills/debug/SKILL.md) | 用证据区分原因，再修复行为 | 自主 |
| [simplify](skills/simplify/SKILL.md) | 理解复杂性承担的责任，再移除多余负担 | 自主 |
| [test-reliability](skills/test-reliability/SKILL.md) | 控制时序、隔离、资源归属和清理 | 自主 |
| [code-review](skills/code-review/SKILL.md) | 独立检查需求、实现和证据 | 自主 |
| [canonical-docs](skills/canonical-docs/SKILL.md) | 让准确说明有合适且明确的归属 | 自主 |
| [decision-records](skills/decision-records/SKILL.md) | 保存并维护无法从代码恢复的决策理由 | 自主 |
| [decision-records-setup](skills/decision-records-setup/SKILL.md) | 基于项目现有文档建立 ADR 约定 | 仅用户 |
| [conventional-commit](skills/conventional-commit/SKILL.md) | 按选定的提交约定表达完整变更意图 | 自主 |

### 模式（Modes）

模式技能提供用于探索、教学和复盘的特定对话状态。

| 技能 | 提供的判断 | 调用方式 |
| --- | --- | --- |
| [grilling](skills/grilling/SKILL.md) | 深入探索想法，不强加目标，不替用户编造动机 | 仅用户 |
| [teach](skills/teach/SKILL.md) | 通过解释与应用建立理解 | 仅用户 |
| [retro](skills/retro/SKILL.md) | 从实际工作中提炼具体改进 | 仅用户 |

任务可以从任意位置介入。明确的故障可以直接诊断，已有的代码改动可以直接审查。让小任务保持精悍。

关于三层架构（Method / Binding / Calibration）契约及编写规范，见 [docs/skill-architecture.md](docs/skill-architecture.md)。

## 安装与调用

```bash
npx skills add Celec7/good-calls
```

*注：对于仍在使用旧路径的项目，`npx skills add Celec7/beyond-code` 依然保持兼容。*

可选择整套安装或按需单独安装。技能正文统一使用英文编写，根目录文档提供中英双语。

### 宿主环境元数据

对于 `decision-records-setup`、`grilling`、`teach` 和 `retro`，其 `SKILL.md` 声明了 `disable-model-invocation: true`，并在 `agents/openai.yaml` 中声明了 `policy.allow_implicit_invocation: false`。这些元数据为支持该规范的宿主环境提供仅用户调用的意图表达。正文同样明确要求用户主动发起。其他技能保持默认的自动发现。

在本地运行以下命令以检查结构规范与链接完整性：

```bash
node scripts/check-skills.mjs
```

## 配合其他技能使用

Good Calls 专注于核心软件工程判断。面对特定垂直领域需求时，可按需搭配 [Matt Pocock 的技能集](https://github.com/mattpocock/skills) 或社区其他工具：

| 辅助技能 | 适用场景 | 与本套件的衔接 |
| --- | --- | --- |
| [writing-for-agents](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md) | 编写技能或 AGENTS.md 等指令 | 补充触发条件描述、信息层级和无效指令删减方法，不作为其他技能的前置条件。 |
| [prototype](https://github.com/mattpocock/skills/blob/main/skills/engineering/prototype/SKILL.md) | 交互探索状态行为，或比较 UI 变体 | 提供具体的原型实验形式；先约定产物留存方式，默认使用临时分支。 |
| [wizard](https://github.com/mattpocock/skills/blob/main/skills/engineering/wizard/SKILL.md) | 引导需要人工配置的敏感步骤 | 生成交互式脚本，仅用于确需人工操作的步骤，脚本可在复用场景下保留。 |
| [handoff](https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md) | 显式交接给新 Agent 或新会话 | 在系统临时目录生成脱敏交接记录，引用现有文档，不另建第二套任务历史。 |

建议根据具体任务按需组合，避免盲目批量安装重叠的技能集。若遇到同名技能（如 `tdd` 或 `code-review`），建议根据项目约定明确保留单一版本。

## 代码、文档与决策

- **代码是实际行为的唯一真源**：需求与经批准的决策描述预期行为。当二者出现冲突时，往往说明实现存在缺陷，而非随意修改需求的理由。测试提供检验依据，但测试本身也可能存在漏洞。
- **文档尊重项目已有结构**：当项目缺乏文档结构且确需建立时，`canonical-docs` 提供标准分层建议。不在初始化阶段创建空目录结构。
- **决策采用轻量化记录**：当持久取舍无法从代码推导时，`decision-records` 采用 `docs/agents/notes/{proposed,implemented,rejected,archived}/YYYY-MM-DD-topic.md`（或仓库已有的 ADR 结构）记录上下文与后果。
- **任务状态保持瞬态**：临时工作笔记保留在会话中。交接确需落地文件时，`plan` 提供可选的 `docs/agents/work/<task>.md` 模板，在任务完成时进行提炼或清理。

## 局限说明

Good Calls 不承诺能够自动消除所有代码缺陷，也无法替代开发者的工程审校：

- **基座模型依赖**：技能的发挥高度取决于底层模型的推理与理解能力。技能提供判断方法，但无法突破模型本身的智能边界。
- **情境收益差异**：技能的收益建立在任务存在真实歧义或非平凡工程取舍的前提下。面对机械简单的编辑，加载技能带来的增益微乎其微。
- **宿主支持程度**：仅用户调用等控制策略依赖宿主环境对 tool-calling 及元数据（`openai.yaml`、frontmatter）的实现，不同客户端的表现可能存在细微差异。

## 开源协议

[MIT](LICENSE)
